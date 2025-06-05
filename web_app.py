from flask import Flask, render_template
from rss_collector import collect_news
from summarizer import initialize_summarizer, summarize_article

app = Flask(__name__)

@app.route("/")
def index():
    articles = collect_news()
    summarizer = initialize_summarizer()

    if summarizer is None:
        return "Fehler beim Laden des Summarizers", 500

    summarized_articles = []

    for article in articles[:10]:  # z.B. nur die ersten 10 Artikel
        summary = summarize_article(summarizer, article["summary"])
        summarized_articles.append({
            "title": article["title"],
            "link": article["link"],
            "summary": summary
        })

    return render_template("index.html", articles=summarized_articles)

if __name__ == "__main__":
    app.run(debug=True)
