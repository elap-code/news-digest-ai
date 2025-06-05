from rss_collector import collect_news
from summarizer import initialize_summarizer, summarize_article


def main():
    print("News Digest AI startet...")
    print("Sammle Nachrichten von RSS-Feeds...")

    articles = collect_news()
    print(f"Gefunden:{len(articles)} Artikel")

    summarizer = initialize_summarizer()
    if summarizer is None:
        print("Fehler beim Laden des Summarizers - Abbruch")
        return

    print("Setup erfolgreich")
    print("Projekt bereit für Entwicklung!")

    for article in articles[:10]:
        print("\n📰 Titel:", article['title'])  # Titel anzeigen
        summary = summarize_article(summarizer, article['summary'])  # KI-Zusammenfassung
        print("📝 Zusammenfassung:", summary)  # Ausgabe der Zusammenfassung

    print("\n✅ Projekt abgeschlossen – News Digest fertig!")


if __name__=="__main__":
    main()