import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import re



def clean_paragraph_text(html: str) -> str:
    """HTML der Paragraphenseite säubern und reinen Text zurückgeben."""
    soup = BeautifulSoup(html, "html.parser")

    # Nervkram entfernen
    for tag in soup(["script", "style", "nav", "header", "footer"]):
        tag.decompose()

    main = soup.find("div", class_="jnhtml") or soup.find("body")
    if not main:
        main = soup

    text = main.get_text(separator="\n", strip=True)

    # Mehrere Leerzeilen & Spaces normalisieren
    text = re.sub(r"\n\s*\n", "\n\n", text)
    text = re.sub(r"[ \t]+", " ", text)

    return text.strip()


def fetch_bgb_range(start_paragraph: int, end_paragraph: int) -> str:
    """
    Holt BGB-Paragraphen im Bereich [start_paragraph, end_paragraph]
    von gesetze-im-internet.de, z.B. 611–630.
    """
    base_url = "https://www.gesetze-im-internet.de/bgb/"
    collected = []

    for num in range(start_paragraph, end_paragraph + 1):
        filename = f"__{num}.html"
        url = urljoin(base_url, filename)
        print(f"Lade: § {num} -> {url}")

        resp = requests.get(url)
        resp.encoding = "utf-8"
        resp.raise_for_status()

        para_text = clean_paragraph_text(resp.text)

        # Zur Sicherheit: Überschrift davor (falls nicht schon enthalten)
        header = f"§ {num} BGB\n"
        collected.append(header + para_text + "\n")

    full_text = "\n\n".join(collected).strip()
    return full_text


# Beispiel: BGB §§ 611–630 holen und in Datei speichern
if __name__ == "__main__":
    text_611_630 = fetch_bgb_range(611, 630)


    output_path = "Gesetze/bgb_611_630.txt"

    with open(output_path, "w", encoding="utf-8") as f:
        f.write(text_611_630)

    print("Gespeichert unter:", output_path)
