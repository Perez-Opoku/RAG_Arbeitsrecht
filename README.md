# Motivation und Forschungsfrage

## Motivation

Juristische Texte sind durch eine komplexe Fachsprache und enorme Textmengen gekennzeichnet. Herkömmliche Suchmethoden (Keyword-Search) stoßen hier schnell an ihre Grenzen, da Laien häufig nicht den exakten juristischen Terminus kennen. Dies zeigt sich besonders deutlich im Arbeitsrecht: Berufseinsteiger und junge Menschen stehen oft vor der Herausforderung, ihre Rechte einzufordern, verfügen aber nicht über das nötige Vokabular, um sich in den Gesetzestexten zurechtzufinden. Diese Informationsasymmetrie kann dazu führen, dass berechtigte Ansprüche aus Unwissenheit nicht geltend gemacht werden.

Das Ziel dieses Projekts ist es, dieses Problem mittels Vektordatenbanken aufzugreifen. Es soll demonstrativ gezeigt werden, wie moderne Technologien genutzt werden können, um komplexes juristisches Wissen auch für Laien zugänglich zu machen. Durch die Umwandlung von Gesetzestexten in hochdimensionale Vektoren (Embeddings) wird eine semantische Suche ermöglicht, die den Sinn einer Anfrage versteht („Ich wurde gefeuert“), statt nur Buchstaben abzugleichen („Kündigung“).

Zudem sollen Visualisierungstechniken genutzt werden, um zu prüfen, ob das Modell juristische Themengebiete – wie etwa das Kündigungsschutzgesetz (KSchG) oder das Mindestlohngesetz (MiLoG) – eigenständig unterscheiden kann. Abschließend wird ein Ausblick darauf gegeben, wie diese Architektur als Basis für Retrieval-Augmented Generation (RAG) dienen kann, um zukünftig generative Antworten zu erzeugen.

## Forschungsfrage

Wie lassen sich deutsche Gesetzestexte mithilfe von modernen Embeddings (Jina AI) und Vektordatenbanken (Chroma DB) semantisch durchsuchbar machen,
und welche latenten Strukturen lassen sich dabei durch Dimensionsreduktion (PCA, t-SNE, UMAP) sichtbar machen?

GITHUB-LINK: https://github.com/Perez-Opoku/RAG_Arbeitsrecht.git

