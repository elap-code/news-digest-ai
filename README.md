# News Digest AI 🤖📰

Ein intelligentes News-Aggregation-Tool, das automatisch Nachrichten von verschiedenen RSS-Feeds sammelt und mit KI-gestützter Textzusammenfassung aufbereitet.

## Features ✨

- **Automatische RSS-Feed-Sammlung** von deutschen und internationalen Nachrichtenquellen
- **KI-basierte Textzusammenfassung** mit dem Modell `facebook/bart-large-cnn` über Hugging Face Transformers
- **Web-Interface** mit Flask für einfache Bedienung
- **Verarbeitung deutscher und englischer Nachrichtentexte** Das verwendete BART-Modell ist primär für englische                Zusammenfassungen optimiert; bei deutschen Texten kann die Qualität variieren
- **Fehlerbehandlung** für robuste Performance

## Nachrichtenquellen 📡

Das Tool sammelt Nachrichten von:
- **Spiegel Online** - Deutsche Nachrichten
- **Tagesschau** - Öffentlich-rechtliche Nachrichten
- **Heise** - Tech-News
- **Zeit Online** - Qualitätsjournalismus
- **The Decoder** - KI und Tech News
- **VentureBeat** - Internationale Tech-Nachrichten

## Installation 🚀

### Voraussetzungen
- Python 3.8 oder höher
- pip (Python Package Manager)
- Internetverbindung für RSS-Feeds und Modell-Download

### Setup

1. **Repository klonen**
```bash
git clone https://github.com/elap-code/news-digest-ai.git
cd news-digest-ai
```

2. **Virtuelle Umgebung erstellen (empfohlen)**
```bash
python -m venv venv
# Windows:
venv\Scripts\activate
# macOS/Linux:
source venv/bin/activate
```

3. **Dependencies installieren**
```bash
pip install -r requirements.txt
```

**Hinweis:** Beim ersten Start wird das KI-Modell heruntergeladen. Der Modelldownload umfasst ca. 1,6 GB. Die Dauer hängt von der Internetverbindung und dem verwendeten System ab.

## Verwendung 💻

### Kommandozeilen-Version
```bash
python main.py
```

Das Programm:
1. Sammelt automatisch Artikel von allen RSS-Feeds
2. Lädt das KI- Modell zur Textzusammenfassung
3. Erstellt Zusammenfassungen der ersten 10 Artikel
4. Zeigt Titel und KI-generierte Zusammenfassungen an

### Web-Version
```bash
python web_app.py
```

Öffnen Sie dann http://localhost:5000 in Ihrem Browser für eine benutzerfreundliche Web-Oberfläche.

### Einzelne Module testen
```bash
# RSS-Collector testen
python rss_collector.py

# Summarizer testen
python summarizer.py
```

## Projektstruktur 📁

```
news-digest-ai/
├── main.py              # Hauptprogramm (Kommandozeile)
├── web_app.py           # Flask Web-Anwendung
├── rss_collector.py     # RSS-Feed Sammlung
├── summarizer.py        # KI-Textzusammenfassung
├── requirements.txt     # Python Dependencies
├── templates/           # HTML Templates (für Web-App)
├── images/             # Projekt-Assets
└── README.md           # Diese Datei
```

## Technische Details 🔧

### Verwendete Technologien
- **Python 3.x** - Hauptprogrammiersprache
- **Transformers (Hugging Face)** - KI-Modell für Textzusammenfassung
- **feedparser** - RSS-Feed Parsing
- **Flask** - Web-Framework
- **PyTorch** - Machine Learning Backend
- **requests** - HTTP-Anfragen

### KI-Modell
- **Modell:** `facebook/bart-large-cnn`
- **Bibliothek:** Hugging Face Transformers
- **Zweck:** Automatische Textzusammenfassung
- **Sprache:** Primär für englische Texte optimiert; deutsche Texte werden ebenfalls verarbeitet, die Qualität kann variieren
- **Ausgabelänge:** konfigurierbar über `min_length` und `max_length`

## Beispielhafte Ausgabe 📋

```
News Digest AI startet...
Sammle Nachrichten von RSS-Feeds...
Gefunden: [Anzahl] Artikel
Setup erfolgreich
Projekt bereit für Entwicklung!

📰 Titel: Neue KI-Entwicklungen in der Automobilindustrie
📝 Zusammenfassung: Automobilhersteller setzen verstärkt auf künstliche Intelligenz für autonomes Fahren. Die neuen Systeme versprechen erhöhte Sicherheit und Effizienz im Straßenverkehr.

📰 Titel: Klimawandel: Neue Studien zeigen dramatische Entwicklung
📝 Zusammenfassung: Wissenschaftler warnen vor beschleunigtem Klimawandel. Neue Daten zeigen stärkere Erwärmung als bisher prognostiziert.
```

## Konfiguration ⚙️

### RSS-Feeds anpassen
Bearbeiten Sie `rss_collector.py` um weitere Feeds hinzuzufügen:

```python
rss_urls = [
    "https://example.com/feed.xml",  # Neuen Feed hier hinzufügen
    # ... bestehende Feeds
]
```

### Zusammenfassungs-Parameter anpassen
In `summarizer.py` können Sie die Länge der Zusammenfassungen ändern:

```python
summary = summarizer(text, max_length=130, min_length=30)
```

## Troubleshooting 🔧

### Häufige Probleme

**Problem:** Modell lädt nicht
```
Lösung: Überprüfen Sie Ihre Internetverbindung und stellen Sie sicher,
dass mehrere GB freier Speicherplatz für Modell und Cache verfügbar sind.
```

**Problem:** RSS-Feed nicht erreichbar
```
Lösung: Einzelne Feeds können temporär offline sein. Das Programm 
überspringt fehlerhafte Feeds automatisch und setzt fort.
```

**Problem:** Speicher-Fehler beim KI-Modell
```
Lösung: Schließen Sie andere speicherintensive Programme. Das KI-Modell benötigt je nach System mehrere GB Arbeitsspeicher.
```

## Roadmap 🛣️

- [ ] Deutsche KI-Modelle für bessere Zusammenfassungen
- [ ] Datenbank-Integration für Artikel-Archivierung
- [ ] E-Mail-Newsletter-Funktion
- [ ] Mobile App
- [ ] Personalisierte Feeds
- [ ] Sentiment-Analyse
- [ ] Kategorisierung der Artikel

## Contributing 🤝

Beiträge sind willkommen! Bitte:

1. Fork das Repository
2. Erstellen Sie einen Feature-Branch (`git checkout -b feature/AmazingFeature`)
3. Commit Ihre Änderungen (`git commit -m 'Add some AmazingFeature'`)
4. Push zum Branch (`git push origin feature/AmazingFeature`)
5. Öffnen Sie einen Pull Request

## Lizenz 📄

Dieses Projekt steht unter der MIT-Lizenz. 
## Autorin 👨‍💻

**Elzbieta Zuzanna Polakowska**
- GitHub: [@elap-code](https://github.com/elap-code)
- E-Mail: ellapolakowska@gmail.com

## Danksagungen 🙏

- Hugging Face für die Transformers-Bibliothek
- Facebook AI für das BART-Modell
- Alle Nachrichtenquellen für ihre RSS-Feeds

