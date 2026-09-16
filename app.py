from flask import Flask, render_template, request, jsonify
import requests
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

API_KEY = os.getenv("NEWS_API_KEY")

NEWS_API_URL = "https://newsapi.org/v2/everything"


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/news")
def get_news():

    topic = request.args.get("topic")

    if not topic:
        return jsonify({
            "error": "Please enter a topic"
        }), 400

    params = {
        "q": topic,
        "language": "en",
        "sortBy": "publishedAt",
        "pageSize": 10,
        "apiKey": API_KEY
    }

    try:

        response = requests.get(
            NEWS_API_URL,
            params=params,
            timeout=10
        )

        data = response.json()

        if response.status_code != 200:
            return jsonify({
                "error": data.get("message", "News API error")
            }), response.status_code

        articles = []

        for article in data.get("articles", []):

            articles.append({
                "title": article.get("title"),
                "description": article.get("description"),
                "source": article.get("source", {}).get("name"),
                "url": article.get("url"),
                "image": article.get("urlToImage")
            })

        return jsonify({
            "topic": topic,
            "articles": articles
        })

    except requests.exceptions.RequestException:
        return jsonify({
            "error": "Unable to connect to News API"
        }), 500

    except Exception:
        return jsonify({
            "error": "Something went wrong"
        }), 500


if __name__ == "__main__":
    app.run(debug=True)