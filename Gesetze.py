import requests
import json
from bs4 import BeautifulSoup
import re

import requests
from bs4 import BeautifulSoup
import re
from urllib.parse import urljoin

def fetch_law_full(law_abbreviation: str) -> str:
    """
    Holt das gesamte Gesetz, indem es alle Paragraphenseiten sammelt.
    Beispiel: "nachwg"
    """
    base_url = f"https://www.gesetze-im-internet.de/{law_abbreviation.lower()}/"
    index_url = urljoin(base_url, "index.html")

    response = requests.get(index_url)
    response.encoding = 'utf-8'
    response.raise_for_status()

    soup = BeautifulSoup(response.text, "html.parser")

    # Titel extrahieren
    h1 = soup.find("h1")
    title = h1.get_text(strip=True) if h1 else law_abbreviation.upper()

    # Alle Links zu den einzelnen Paragraphen finden
    content_links = []
    for a in soup.find_all("a", href=True):
        href = a["href"]
        if href.startswith("__") and href.endswith(".html"):
            content_links.append(urljoin(base_url, href))

    if not content_links:
        raise ValueError("Keine Paragraphenseiten gefunden – Struktur der Seite hat sich evtl. geändert.")

    paragraphs = []

    # Jede Paragraphenseite laden
    for link in content_links:
        page = requests.get(link)
        page.encoding = 'utf-8'
        page.raise_for_status()

        psoup = BeautifulSoup(page.text, "html.parser")

        # Relevante Elemente entfernen
        for tag in psoup(['script', 'style', 'nav', 'header', 'footer']):
            tag.decompose()

        # Haupttext
        main = psoup.find("div", class_="jnhtml") or psoup.find("body")
        text = main.get_text(separator="\n", strip=True)

        paragraphs.append(text)

    # Alles zusammensetzen
    full_text = title + "\n\n" + "\n\n".join(paragraphs)
    return full_text


# TEST
NachwG_data = fetch_law_full("nachwg")
print(NachwG_data)
with open("Gesetze/NachwG.txt", "w", encoding="utf-8") as f:
    f.write(NachwG_data)

gesetze = ["BUrlG","entgfg","TzBfG","AGG","MiLoG","ArbSchG", "BetrVG","ArbzG","KSchG"]



for i in gesetze:
    data = fetch_law_full(i)
    print(i)
    with open(f"Gesetze/{i}.txt", "w", encoding="utf-8") as f:
        f.write(data)
    print(f"{i} gespeichert.")


