from flask import Flask, render_template, request, jsonify
import requests
import os

from dotenv import load_dotenv
from google import genai


# Load environment variables from .env
load_dotenv()


app = Flask(__name__)


# --------------------------------------------------
# API KEYS
# --------------------------------------------------

NEWS_API_KEY = os.getenv("NEWS_API_KEY")
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")


# Check whether API keys exist
if not NEWS_API_KEY:
    print("WARNING: NEWS_API_KEY is not set.")

if not GEMINI_API_KEY:
    print("WARNING: GEMINI_API_KEY is not set.")


# --------------------------------------------------
# GEMINI CLIENT
# --------------------------------------------------

client = genai.Client(
    api_key=GEMINI_API_KEY
)


# --------------------------------------------------
# NEWS API
# --------------------------------------------------

NEWS_API_URL = "https://newsapi.org/v2/everything"


# --------------------------------------------------
# HOME PAGE
# --------------------------------------------------

@app.route("/")
def home():
    return render_template("index.html")


# --------------------------------------------------
# GEMINI FUNCTION
# Convert natural-language question
# into useful news search queries
# --------------------------------------------------

def generate_search_queries(user_question):

    prompt = f"""
You are a news search query generator.

The user may write their question in:
- Simple English
- Informal English
- Broken English
- Conversational English

Your task is to understand the user's intent
and generate exactly 5 short search queries that
can be sent to a news search API.

User question:
{user_question}

Rules:
1. Identify the important people, companies,
   technologies, countries, events, or topics.
2. Create concise search queries.
3. Do not answer the user's question.
4. Do not provide explanations.
5. Return ONLY the 5 search queries.
6. Put each query on a separate line.
"""

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    text = response.text.strip()

    queries = text.split("\n")

    # Clean the generated queries
    cleaned_queries = []

    for query in queries:

        query = query.strip()

        # Remove numbering such as:
        # 1. Python news
        # 2. AI jobs
        if query:
            query = query.lstrip("1234567890.-) ")

            if query:
                cleaned_queries.append(query)

    # Return maximum 3 queries
    return cleaned_queries[:5]


# --------------------------------------------------
# NEWS SEARCH
# --------------------------------------------------

@app.route("/news")
def get_news():

    user_question = request.args.get("question", "").strip()

    # Check user input
    if not user_question:

        return jsonify({
            "error": "Please enter a news question."
        }), 400


    # Check API keys
    if not NEWS_API_KEY:

        return jsonify({
            "error": "News API key is not configured."
        }), 500


    if not GEMINI_API_KEY:

        return jsonify({
            "error": "Gemini API key is not configured."
        }), 500


    try:

        # --------------------------------------------------
        # STEP 1:
        # Ask Gemini to understand the question
        # --------------------------------------------------

        queries = generate_search_queries(
            user_question
        )


        if not queries:

            return jsonify({
                "error": "Could not generate search queries."
            }), 500


        # --------------------------------------------------
        # STEP 2:
        # Search NewsAPI using each query
        # --------------------------------------------------

        all_articles = []


        for query in queries:

            params = {

                "q": query,

                "language": "en",

                "sortBy": "publishedAt",

                "pageSize": 10,

                "apiKey": NEWS_API_KEY
            }


            response = requests.get(
                NEWS_API_URL,
                params=params,
                timeout=10
            )


            data = response.json()


            # Check NewsAPI response
            if response.status_code != 200:

                return jsonify({

                    "error": data.get(
                        "message",
                        "News API request failed."
                    )

                }), response.status_code


            articles = data.get(
                "articles",
                []
            )


            all_articles.extend(
                articles
            )


        # --------------------------------------------------
        # STEP 3:
        # Remove duplicate articles
        # --------------------------------------------------

        unique_articles = {}


        for article in all_articles:

            article_url = article.get("url")


            if article_url:

                unique_articles[
                    article_url
                ] = article


        # --------------------------------------------------
        # STEP 4:
        # Prepare articles for frontend
        # --------------------------------------------------

        final_articles = []


        for article in unique_articles.values():

            source = article.get(
                "source",
                {}
            )


            final_articles.append({

                "title": article.get(
                    "title",
                    "No title"
                ),

                "description": article.get(
                    "description",
                    "No description available."
                ),

                "source": source.get(
                    "name",
                    "Unknown"
                ),

                "author": article.get(
                    "author"
                ),

                "publishedAt": article.get(
                    "publishedAt"
                ),

                "url": article.get(
                    "url"
                ),

                "image": article.get(
                    "urlToImage"
                )
            })


        # --------------------------------------------------
        # STEP 5:
        # Send response to frontend
        # --------------------------------------------------

        return jsonify({

            "question": user_question,

            "queries": queries,

            "articles": final_articles

        })


    # --------------------------------------------------
    # Handle API connection errors
    # --------------------------------------------------

    except requests.exceptions.RequestException:

        return jsonify({

            "error":
            "Unable to connect to NewsAPI."

        }), 500


    # --------------------------------------------------
    # Handle all other errors
    # --------------------------------------------------

    except Exception as e:

        print("ERROR:", e)

        return jsonify({

            "error":
            "Something went wrong while processing your request."

        }), 500


# --------------------------------------------------
# RUN FLASK
# --------------------------------------------------

if __name__ == "__main__":

    app.run(
        debug=True
    )