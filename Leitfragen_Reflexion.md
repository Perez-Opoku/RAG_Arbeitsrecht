# Stellung und Beantwortung der Leitfragen

- **Welche Art von Daten oder Szenario möchten Sie untersuchen?**

  Wir untersuchen **unstrukturierte Textdaten** in Form von **deutschen Gesetzestexten**.  
  Der inhaltliche Fokus liegt auf **Arbeitnehmerrechten**. Diese sind auch im Ordner *Gesetze* zu finden.
  
- **Welche Struktur erwarten Sie im Embeddingraum?**
  
  Wir erwarten eine klare Abgrenzung zu anderen Gesetzestexten, da diese unterschiedliche Themenfelder behandeln.  
  Gleichzeitig gehen wir von einer hohen semantischen Ähnlichkeit innerhalb der betrachteten Gesetze aus, da sie sich auf denselben thematischen Kontext und vergleichbare rechtliche Inhalte beziehen.

- **Welche Methode oder Modellfamilie wollen Sie dafür einsetzen?**

  ## Embedding

  Zum Berechnen der Embeddings benutzen wir **Jina Embeddings v3**, ein **transformer-basiertes Embedding-Modell**, ähnlich wie BERT.
  
  Wir haben dieses Modell aus drei Gründen gewählt:

  Sprachverständnis:  
  Es ist explizit für mehrsprachige Aufgaben inklusive Deutsch optimiert und liefert oft bessere Ergebnisse als generische Modelle.

  Kontextlänge:  
  Es unterstützt eine Sequenzlänge von bis zu 8192 Token, was für juristische Schachtelsätze essenziell ist, um den Kontext nicht abzuschneiden.

  Task-Specific Embeddings:  
  Das Modell wurde speziell für Retrieval-Tasks trainiert, was für unseren Anwendungsfall ideal ist.

  ## Vektordatenbank

  Zur Speicherung und für das effiziente Retrieval implementieren wir **Chroma DB**.

  Effiziente Indexierung:  
  Chroma nutzt den HNSW-Algorithmus (Hierarchical Navigable Small World), der eine skalierbare und extrem schnelle Approximate-Nearest-Neighbor-(ANN)-Suche ermöglicht, statt jeden Vektor einzeln vergleichen zu müssen.

  Metadaten:  
  Wir können zu jedem Vektor den Gesetzestext und den Paragraphen als Payload speichern, was für die spätere Antwortgenerierung notwendig ist.

  ## Analyse & Visualisierung

  Um die Struktur der Embeddings zu überprüfen, nutzen wir Dimensionsreduktionsverfahren. Wir vergleichen PCA (linear) mit t-SNE und UMAP (nicht-linear), um zu zeigen, dass die semantischen Zusammenhänge im Vektorraum komplexer Natur sind und durch lineare Verfahren allein nicht ausreichend abgebildet werden können.

  ## Reflexion zur letzten Leitfrage

  **Welche Limitationen sind erkennbar?**
  ### Chunks
  Eine der größten technischen Limitationen ist das Aufteilen der Gesetzestexte in feste Abschnitte (Chunks). Juristische Texte sind stark hierarchisch aufgebaut und referenzieren sich gegenseitig; dieser Kontext geht bei einfachem Retrieval auf einer Vektordatenbank     verloren. Zudem führen arbiträre, harte Grenzen beim Chunking dazu, dass die jeweiligen Embeddings nicht unbedingt die besten Grenzen für den bestmöglichen Kontext erhalten.
  ### Retrieval
  Im Gegensatz zur klassischen Stichwortsuche ist bei der Vektorsuche schwer nachvollziehbar, warum ein bestimmter Paragraph als „relevant“ eingestuft wurde. Ein Paragraph kann eine hohe Cosine-Similarity aufweisen, weil er thematisch ähnlich klingt, aber rechtlich       genau das Gegenteil aussagt. Das System versteht lediglich semantische Nähe.

  Eine andere Art von Limitatation ist die Domain Gap
  Hier der Unterschied zwischen der Sprache der Nutzer und der Sprache der Gesetze.

  Das Problem: Laien suchen nach „Ich wurde gefeuert“. Im Gesetz steht aber „Kündigung des Arbeitsverhältnisses“.

  Die Folge: Obwohl das Embedding-Modell Ähnlichkeiten erkennt, funktioniert die Suche viel besser, wenn man die Fachbegriffe kennt.

  Für Experten und Anwälte ein Vorteil, sie können sich super schnell einlesen und bekommen bessere Ergebnisse. Wer keine Ahnung hat (unsere Zielgruppe), bekommt schlechtere Ergebnisse. Das System verstärkt also ungewollt den Vorteil, den Experten ohnehin schon haben.
