# AI News Search Application

## 1. Project Overview

**AI News Search** is a Flask-based web application that allows users to search for news using **natural-language questions**.

Instead of requiring the user to enter only short keywords, the application uses **Gemini** to understand the user's question and generate concise search queries. These queries are then sent to **NewsAPI** to retrieve relevant news articles.

### Example

User enters:

```text
Latest news on job layoffs because of GPT-6 Astra
```

The application can convert this into search queries such as:

```text
GPT-6 Astra
AI job layoffs
GPT-6 layoffs
```

These queries are then used to search NewsAPI.

---

# 2. Main Objective

The main objective of this project is to learn how to integrate:

* Flask
* Frontend and backend communication
* REST APIs
* API requests and responses
* JSON
* API keys
* Environment variables
* Gemini LLM
* NewsAPI
* Error handling
* Git and GitHub
* Secure API-key management

---

# 3. Technologies Used

| Technology    | Purpose                                                             |
| ------------- | ------------------------------------------------------------------- |
| Python        | Main programming language                                           |
| Flask         | Backend web framework                                               |
| HTML          | Webpage structure                                                   |
| CSS           | Webpage styling                                                     |
| JavaScript    | Frontend logic and API communication                                |
| Gemini API    | Understands natural-language questions and generates search queries |
| NewsAPI       | Retrieves news articles                                             |
| Requests      | Sends HTTP requests from Python                                     |
| python-dotenv | Loads environment variables from `.env`                             |
| JSON          | Data exchange format                                                |
| Git           | Version control                                                     |
| GitHub        | Code repository                                                     |

---

# 4. Application Architecture

```text
                    USER
                      |
                      ↓
              HTML/CSS/JavaScript
                      |
                      ↓
              Flask Backend
                      |
             User's Question
                      |
                      ↓
                Gemini API
                      |
          Generate Search Queries
                      |
                      ↓
                  NewsAPI
                      |
              News Articles
                      |
                      ↓
              Flask Backend
                      |
              Process JSON Data
                      |
                      ↓
             HTML/JavaScript
                      |
                      ↓
                 USER
```

---

# 5. Complete Request Flow

Suppose the user enters:

```text
What is happening with AI jobs in India?
```

The flow is:

```text
User
 ↓
Frontend
 ↓
GET /news?question=What is happening with AI jobs in India?
 ↓
Flask
 ↓
Gemini API
 ↓
Generate search queries
 ↓
India AI jobs
AI jobs India
Artificial intelligence employment India
 ↓
NewsAPI
 ↓
JSON response containing articles
 ↓
Flask processes the articles
 ↓
Frontend displays the articles
```

---

# 6. Project Folder Structure

```text
news_ai_project/
│
├── app.py
├── .env
├── .gitignore
├── requirements.txt
│
└── templates/
    └── index.html
```

---

# 7. File Explanation

## `app.py`

This is the main Flask backend file.

It:

* Starts the Flask application
* Receives the user's question
* Sends the question to Gemini
* Gets search queries from Gemini
* Sends the queries to NewsAPI
* Receives news articles
* Processes the JSON response
* Removes duplicate articles
* Sends the final data to the frontend

---

## `index.html`

This is the frontend.

It:

* Displays the search box
* Takes the user's question
* Sends the question to Flask
* Receives the response
* Displays generated search queries
* Displays news articles
* Shows loading messages
* Shows errors

---

## `.env`

The `.env` file stores secret configuration values such as API keys.

Example:

```text
NEWS_API_KEY=your_newsapi_key
GEMINI_API_KEY=your_gemini_api_key
```

The actual keys should be stored only on your local machine or in a secure deployment environment.

---

## `.gitignore`

`.gitignore` tells Git which files should not be uploaded to GitHub.

Example:

```text
venv/
__pycache__/
*.pyc
.env
```

The important line is:

```text
.env
```

This prevents your API keys from accidentally being committed to GitHub.

---

## `requirements.txt`

This file contains the Python packages required by the project.

```text
Flask
requests
python-dotenv
google-genai
```

Install them using:

```bash
pip install -r requirements.txt
```

---

# 8. How to Get the Gemini API Key

Gemini API access can be set up through **Google AI Studio**.

Open:

[Google AI Studio](https://aistudio.google.com/)

Basic process:

```text
Google AI Studio
       ↓
Sign in
       ↓
Open API Keys
       ↓
Create API Key
       ↓
Copy the API Key
       ↓
Store it in .env
```

Example:

```text
GEMINI_API_KEY=AIzaSyXXXXXXXXXXXX
```

Do **not** share your actual API key in:

* GitHub
* Public websites
* Screenshots
* Chat messages
* Frontend JavaScript

---

# 9. How to Get the NewsAPI Key

Create an account with NewsAPI and obtain an API key from its developer dashboard.

Then add it to `.env`:

```text
NEWS_API_KEY=your_actual_newsapi_key
```

Your project therefore uses two external APIs:

```text
Gemini API
     ↓
Understands the user's question

NewsAPI
     ↓
Retrieves news articles
```

---

# 10. Gemini API vs NewsAPI

These two APIs have different responsibilities.

### Gemini API

Gemini is used for:

```text
Understanding the user's natural-language question
                  ↓
Generating useful search queries
```

### NewsAPI

NewsAPI is used for:

```text
Search query
     ↓
NewsAPI
     ↓
News articles
```

Gemini does **not** retrieve the news articles in this project.

NewsAPI does **not** understand the user's entire natural-language question in the same way an LLM does.

---

# 11. What is an API?

API stands for:

**Application Programming Interface**

In simple words:

> An API allows one application or service to communicate with another application or service.

Example:

```text
Our Flask Application
        |
        | API Request
        ↓
    Gemini API
        |
        | API Response
        ↓
Our Flask Application
```

---

# 12. What is an API Key?

An API key is a credential provided by an API service.

It is used by the service to identify and authenticate the application making requests.

Example:

```text
GEMINI_API_KEY=xxxxxxxx
```

The key is not the API itself.

```text
API
↓
The service/interface we communicate with

API Key
↓
Credential used to access the service
```

---

# 13. Why Does This Project Need Two API Keys?

Because the application communicates with two external services.

```text
                 Flask
                /     \
               /       \
              ↓         ↓
          Gemini       NewsAPI
             ↓            ↓
        Query          News
        generation     articles
```

Therefore:

```text
GEMINI_API_KEY
NEWS_API_KEY
```

are stored separately.

---

# 14. Why Use `.env`?

Instead of writing the API key directly in Python:

```python
GEMINI_API_KEY = "AIzaSyXXXXXXXX"
```

we use:

```text
GEMINI_API_KEY=AIzaSyXXXXXXXX
```

inside `.env`.

Then Python reads it:

```python
import os
from dotenv import load_dotenv

load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
```

This keeps sensitive credentials separate from the source code.

---

# 15. How Gemini Is Connected to Flask

The application imports the Google GenAI library:

```python
from google import genai
```

The API key is loaded:

```python
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
```

A Gemini client is created:

```python
client = genai.Client(
    api_key=GEMINI_API_KEY
)
```

The application can then send a prompt to Gemini.

Example:

```python
response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents=prompt
)
```

The response can then be processed by Python.

---

# 16. Why Did We Add Gemini?

Originally, the application could directly send the user's input to NewsAPI.

For example:

```text
User:
latest news on AI jobs in India
```

The application would directly search NewsAPI.

The problem is that users can write questions in many ways.

For example:

```text
What's happening with AI jobs in India?

Tell me about AI employment in India.

Are AI companies reducing jobs in India?

What is the latest situation with AI jobs?
```

Gemini helps convert these natural-language questions into concise search queries.

---

# 17. Gemini's Role

Gemini receives:

```text
User's natural-language question
```

and produces:

```text
Search query 1
Search query 2
Search query 3
```

For example:

```text
User:
What is happening with AI jobs in India?

Gemini:
India AI jobs
AI jobs India
Artificial intelligence employment India
```

These queries are then sent to NewsAPI.

---

# 18. Important: Gemini Does Not Make Up the News

The project separates two responsibilities.

```text
Gemini
↓
Understands the question
↓
Generates search queries

NewsAPI
↓
Searches news sources
↓
Returns articles
```

Gemini is not being used as the source of the news articles.

The actual articles come from NewsAPI.

This is important when explaining the project in an interview.

---

# 19. Flask Endpoint

The application creates:

```python
@app.route("/news")
def get_news():
```

This creates the application's `/news` endpoint.

The frontend sends:

```text
/news?question=AI jobs in India
```

Flask receives the question:

```python
user_question = request.args.get(
    "question",
    ""
).strip()
```

---

# 20. Query Parameter

In:

```text
/news?question=AI jobs in India
```

the part:

```text
question=AI jobs in India
```

is a query parameter.

It allows the frontend to send information to the backend through the URL.

---

# 21. GET Request

The frontend uses:

```javascript
fetch(
    `/news?question=${encodeURIComponent(question)}`
);
```

This sends a GET request to Flask.

The basic flow is:

```text
Browser
   |
   | GET request
   ↓
Flask /news
```

---

# 22. NewsAPI Request

For each generated query, Flask creates parameters:

```python
params = {
    "q": query,
    "language": "en",
    "sortBy": "publishedAt",
    "pageSize": 10,
    "apiKey": NEWS_API_KEY
}
```

Then it sends the request:

```python
response = requests.get(
    NEWS_API_URL,
    params=params,
    timeout=10
)
```

---

# 23. What Does `requests.get()` Do?

`requests.get()` sends an HTTP GET request from Python to another server.

Example:

```python
response = requests.get(url)
```

In this project:

```text
Flask
 ↓
requests.get()
 ↓
NewsAPI
```

---

# 24. What Is JSON?

JSON stands for:

**JavaScript Object Notation**

It is a common format for exchanging data between applications.

Example:

```json
{
    "title": "Example News",
    "description": "News description",
    "source": "Example Source"
}
```

The API returns JSON, and Python processes that JSON.

---

# 25. Processing the News Response

The application gets the JSON response:

```python
data = response.json()
```

Then it extracts the articles:

```python
articles = data.get(
    "articles",
    []
)
```

The application extracts information such as:

```text
Title
Description
Source
Author
Published date
Article URL
Image
```

---

# 26. Removing Duplicate Articles

Because the application searches multiple queries, the same article can sometimes appear more than once.

The project removes duplicates using the article URL.

```python
unique_articles = {}

for article in all_articles:
    article_url = article.get("url")

    if article_url:
        unique_articles[article_url] = article
```

The URL acts as a unique identifier.

---

# 27. Final Response

Flask sends the processed data back as JSON:

```python
return jsonify({
    "question": user_question,
    "queries": queries,
    "articles": final_articles
})
```

The frontend receives this response.

```text
Flask
  ↓
JSON response
  ↓
JavaScript
  ↓
Display news
```

---

# 28. Frontend Communication

JavaScript uses:

```javascript
fetch()
```

to communicate with Flask.

Basic flow:

```text
HTML
 ↓
JavaScript
 ↓
fetch()
 ↓
Flask
 ↓
JSON response
 ↓
JavaScript
 ↓
HTML page
```

---

# 29. Error Handling

The application handles several possible errors.

### Empty question

```text
User submits nothing
        ↓
Flask returns 400
```

### Missing NewsAPI key

```text
NEWS_API_KEY not found
        ↓
Flask returns error
```

### Missing Gemini key

```text
GEMINI_API_KEY not found
        ↓
Flask returns error
```

### API connection failure

```text
NewsAPI cannot be reached
        ↓
Exception occurs
        ↓
Error response
```

### No articles

```text
API returns zero articles
        ↓
Frontend displays
"No articles found"
```

---

# 30. Why Use `python-dotenv`?

`python-dotenv` loads values from the `.env` file into environment variables.

Example:

```python
from dotenv import load_dotenv

load_dotenv()
```

Then:

```python
os.getenv("GEMINI_API_KEY")
```

can retrieve the value.

---

# 31. `.env` vs `.gitignore`

These two files have different purposes.

### `.env`

Stores configuration/secrets.

```text
GEMINI_API_KEY=xxxxx
NEWS_API_KEY=xxxxx
```

### `.gitignore`

Tells Git what not to track.

```text
.env
```

So:

```text
.env
   ↓
Contains secret

.gitignore
   ↓
Prevents Git from tracking .env
```

---

# 32. Why Should the API Key Not Be in Frontend JavaScript?

Frontend JavaScript is sent to the user's browser.

Therefore, users can inspect the browser's source/code.

If we put:

```javascript
const API_KEY = "xxxxxxxx";
```

in frontend code, the key could become visible.

Instead:

```text
Frontend
   ↓
Flask backend
   ↓
Gemini / NewsAPI
```

The API keys remain on the backend.

---

# 33. How the Project Uses REST APIs

The project communicates with web APIs using HTTP requests.

Examples include:

```text
GET
POST
PUT
PATCH
DELETE
```

This project mainly uses **GET requests** to retrieve information.

The architecture can be described as:

> A Flask-based web application that integrates external REST APIs.

---

# 34. API vs Endpoint

### API

A complete interface/service that allows applications to communicate.

### Endpoint

A specific URL through which a particular API operation can be accessed.

Example:

```text
/news
```

is an endpoint created by our Flask application.

The external NewsAPI also provides its own endpoints.

---

# 35. API Integration Process

The general API integration process used in this project is:

```text
1. Identify the required functionality
             ↓
2. Find a suitable API
             ↓
3. Read official documentation
             ↓
4. Get required credentials
             ↓
5. Identify endpoint
             ↓
6. Identify HTTP method
             ↓
7. Identify parameters
             ↓
8. Send request
             ↓
9. Receive JSON response
             ↓
10. Process the response
             ↓
11. Display/use the data
```

---

# 36. How to Run the Project

## Step 1: Create a virtual environment

```bash
python -m venv venv
```

Activate it on Windows:

```bash
venv\Scripts\activate
```

---

## Step 2: Install dependencies

```bash
pip install -r requirements.txt
```

---

## Step 3: Create `.env`

Create a file named:

```text
.env
```

Add:

```text
NEWS_API_KEY=your_newsapi_key
GEMINI_API_KEY=your_gemini_api_key
```

---

## Step 4: Run Flask

```bash
python app.py
```

You should see Flask running locally.

Open the local address shown by Flask in your browser.

---

# 37. Example Usage

User enters:

```text
Tell me the latest news about AI jobs in India
```

Gemini generates search queries:

```text
AI jobs India
India artificial intelligence employment
AI companies India jobs
```

NewsAPI searches these queries.

The application then displays the retrieved articles.

---

# 38. One-Minute Interview Explanation

> I developed an AI News Search application using Python, Flask, HTML, CSS, and JavaScript. The application allows users to enter news questions in natural language. I integrated Gemini to understand the user's question and generate concise search queries. These queries are then sent to NewsAPI to retrieve relevant news articles. The Flask backend processes the JSON response, removes duplicate articles, and sends the required information to the frontend. I also learned API-key-based authentication and stored the Gemini and NewsAPI keys securely using environment variables and a `.env` file.

---

# 39. Interview Questions and Answers

## Q1. Tell me about your project.

> I developed an AI News Search application using Flask. Users can enter a natural-language news question. The Flask backend sends the question to Gemini, which generates concise search queries. I then use those queries with NewsAPI to retrieve news articles. The backend processes the JSON response and sends the results to the frontend.

---

## Q2. Why did you use Gemini?

> I used Gemini to understand natural-language questions and convert them into concise search queries that can be used with the news API.

---

## Q3. Why didn't you directly send the user's question to NewsAPI?

> Directly sending a long conversational question may not always produce useful search results. Gemini helps extract the important topics and generate shorter search queries.

---

## Q4. What is Gemini's role?

> Gemini acts as the natural-language understanding layer. It converts the user's question into search queries.

---

## Q5. What is NewsAPI's role?

> NewsAPI retrieves news articles based on the search queries generated by Gemini.

---

## Q6. Did you create Gemini?

> No. Gemini is an external Google AI service. I integrated its API into my Flask application.

---

## Q7. Did you create NewsAPI?

> No. NewsAPI is an external news service. I integrated it into my application.

---

## Q8. How did you get the Gemini API key?

> I created the API key through Google AI Studio and stored it as an environment variable instead of hardcoding it in my source code.

---

## Q9. Where did you store the API key?

> I stored it in a `.env` file during local development and added `.env` to `.gitignore` so that the secret would not be committed to Git.

---

## Q10. Why shouldn't API keys be uploaded to GitHub?

> API keys are credentials. If they become public, another person could potentially use the credentials and consume the associated API access or quota.

---

## Q11. What is an API key?

> An API key is a credential provided by an API service to identify or authorize requests from an application.

---

## Q12. What is JSON?

> JSON is a lightweight data format commonly used for exchanging data between applications and APIs.

---

## Q13. What is Flask?

> Flask is a lightweight Python web framework. I used it to create the backend and API endpoint for my application.

---

## Q14. What is the `/news` endpoint?

> `/news` is an endpoint created in my Flask application. It receives the user's news question, processes it using Gemini and NewsAPI, and returns the results.

---

## Q15. How does frontend communicate with backend?

> The frontend uses JavaScript's `fetch()` function to send an HTTP request to the Flask backend. Flask processes the request and returns a JSON response, which JavaScript uses to update the webpage.

---

## Q16. What is the complete architecture?

> The flow is: User → Frontend → Flask Backend → Gemini API → Search Queries → NewsAPI → JSON Response → Flask → Frontend.

---

## Q17. What happens if the API key is missing?

> The application checks whether the required API key is available. If it is missing, the application returns an appropriate error instead of making the API request.

---

## Q18. What happens if NewsAPI is unavailable?

> The application catches the request exception and returns an error message to the frontend.

---

## Q19. Why did you use `requests`?

> I used the Python `requests` library to send HTTP requests from my Flask backend to external APIs.

---

## Q20. What is `python-dotenv`?

> `python-dotenv` is a Python package that loads variables from a `.env` file into the application's environment.

---

# 40. Scenario-Based Interview Questions

## Scenario 1: The API key is exposed on GitHub. What would you do?

Answer:

> I would immediately revoke or regenerate the exposed API key through the provider, remove the secret from the repository and relevant history if necessary, create a new key, and store it securely using environment variables.

---

## Scenario 2: Gemini generates poor search queries. What would you do?

Answer:

> I would improve the prompt used for query generation and add rules for concise, relevant queries. I could also validate the generated output before sending it to NewsAPI.

---

## Scenario 3: NewsAPI returns duplicate articles.

Answer:

> Since multiple search queries can return the same article, I can use the article URL as a unique identifier and remove duplicate URLs before displaying the results.

---

## Scenario 4: The user enters an empty question.

Answer:

> I validate the input before making any API request. If the question is empty, I return a 400 error and ask the user to enter a question.

---

## Scenario 5: Gemini is unavailable.

Answer:

> The application should catch the API error and return a meaningful error message instead of crashing.

---

# 41. Important Concepts Learned

Through this project, I learned:

```text
Python
   ↓
Flask
   ↓
HTTP
   ↓
REST APIs
   ↓
API Endpoints
   ↓
GET Requests
   ↓
Query Parameters
   ↓
API Keys
   ↓
Environment Variables
   ↓
JSON
   ↓
Gemini LLM
   ↓
NewsAPI
   ↓
Frontend-Backend Communication
   ↓
Error Handling
   ↓
Git/GitHub
```

---

# 42. Important Interview Terminology

Use these terms correctly.

### Instead of:

> I extracted the Gemini API.

Say:

> I integrated the Gemini API.

### Instead of:

> I created Gemini API.

Say:

> I created an API key and integrated the Gemini API into my application.

### Instead of:

> Gemini gives me the news.

Say:

> Gemini generates search queries, while NewsAPI retrieves the news articles.

### Instead of:

> `.gitignore` hides my API key.

Say:

> `.gitignore` prevents the `.env` file from being tracked by Git.

---

# 43. Simple Memory Formula

Remember the entire project using:

```text
USER
 ↓
QUESTION
 ↓
FLASK
 ↓
GEMINI
 ↓
SEARCH QUERIES
 ↓
NEWSAPI
 ↓
JSON
 ↓
FLASK
 ↓
FRONTEND
 ↓
NEWS ARTICLES
```

For API-key security:

```text
API KEY
   ↓
.env
   ↓
os.getenv()
   ↓
Flask Backend
   ↓
External API
```

---

# 44. Final Project Summary

This project demonstrates how an application can combine an **LLM** with a traditional **REST API**.

```text
LLM
↓
Understands user intent
↓
Generates search queries
↓
Traditional News API
↓
Retrieves actual articles
↓
Flask
↓
Processes the data
↓
Frontend
↓
Displays results
```

The main learning outcome is understanding how **frontend, backend, LLM APIs, REST APIs, API keys, JSON, and external services communicate with each other in a real application**.
