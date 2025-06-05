#RSS Feed Sammler holt Nachrichten von verschiedenen Websites

import feedparser
import requests

def collect_news():
    rss_urls = [
        "https://www.spiegel.de/schlagzeilen/index.rss",
        "https://www.tagesschau.de/xml/rss2/",
        "https://heisse.de/rss/heise-atom.xml",
        "https://www.zeit.de/news/index",
        "https://the-decoder.de/feed/",
        "https://venturebeat.com/ai/feed"
    ]

    all_articles = []

    for url in rss_urls:
        try:
            feed = feedparser.parse(url)
            for entry in feed.entries:
                article = {
                    "title":entry.title,
                    "summary":entry.summary,
                    "link":entry.link,
                    "published":entry.published
                }
                all_articles.append(article)
        except Exception as e:
            print(f"Fehler beim Laden von {url}:{e}")      
            continue
    return all_articles  