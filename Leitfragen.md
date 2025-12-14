# Stellung und beantwortung der Leitfragen

- **Welche Art von Daten oder Szenario möchten Sie untersuchen?**

  Wir untersuchen **unstrukturierte Textdaten** in Form von **deutschen Gesetzestexten**. 
  Der inhaltliche Fokus liegt auf **Arbeitnehmerrechten**, diese sind auch im Ordner Gesetze zu finden.
  
- **Welche Struktur erwarten Sie im Embeddingraum?**
  
  Wir erwarten eine klare Trennung  zu anderen Gesetzen, aufgrund der unterschiedlichen Themen welche diese behandeln
  und eine große ähnlichkeit in den Gesetzen zueinander, aufgrund der gleichen Semantik und Thema
  
- **Welche Methode oder Modellfamilie wollen Sie dafür einsetzen?**
  
  Zum Berechnen der Embeddings benutzen wir Jina Embeddings v3 Ein **Transformer-basiertes Embedding-Modell**
  ähnlich wie BERT.
  
  Wir haben dieses Modell aus drei Gründen gewählt:

  Sprachverständnis: Es ist explizit für mehrsprachige Aufgaben inklusive Deutsch optimiert und liefert oft bessere Ergebnisse als generische Modelle.

  Kontextlänge: Es unterstützt eine Sequenzlänge von bis zu 8192 Token, was für juristische Schachtelsätze essenziell ist, um den Kontext nicht abzuschneiden.

  Task-Specific Embeddings: Das Modell wurde speziell für Retrieval-Tasks trainiert, was für unseren Anwendungsfall Datenbank ideal ist
