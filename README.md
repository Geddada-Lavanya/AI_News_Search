# News Search App using Flask and NewsAPI

## 1. Project Title

**News Search App using Flask and NewsAPI**

---

## 2. Project Overview

The News Search App is a web application that allows users to search for news articles based on a topic or keyword.

For example, the user can search for:

* Python
* Artificial Intelligence
* Machine Learning
* Technology
* Cricket

The application uses **Flask** as the backend and integrates the **NewsAPI** third-party REST API to retrieve news articles.

The NewsAPI requires an **API key**, so the project also demonstrates how to securely store and use an API key using an `.env` file and environment variables.

---

# 3. Why Did I Build This Project?

I built this project to learn how to integrate a **third-party API that requires an API key** into a Flask application.

Before this project, I learned API integration using a public API that did not require authentication. I wanted to understand the next important concept: **API-key-based authentication**.

Through this project, I learned:

* How to find an API
* How to read API documentation
* How to obtain an API key
* What an API key is
* How to store an API key securely
* How to use `.env`
* How to use environment variables
* How to send GET requests
* How to pass query parameters
* How to receive JSON responses
* How to process JSON data
* How Flask communicates with an external API
* How to handle API errors
* Why secrets should not be uploaded to GitHub

---

# 4. Technologies Used

| Technology    | Purpose                                    |
| ------------- | ------------------------------------------ |
| Python        | Backend programming                        |
| Flask         | Backend web framework                      |
| HTML          | Web page structure                         |
| CSS           | Web page styling                           |
| JavaScript    | Frontend interaction                       |
| Requests      | Sending HTTP requests                      |
| python-dotenv | Loading variables from `.env`              |
| NewsAPI       | Providing news data                        |
| JSON          | Data exchange format                       |
| Git/GitHub    | Version control and source-code management |

---

# 5. Main Features

* Search news by topic
* Get latest relevant articles
* Display article title
* Display article description
* Display source
* Display article image when available
* Open the original article
* API integration using Flask
* API-key authentication
* Error handling
* Secure API-key storage

---

# 6. Project Structure

```text
news_api_project/
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

# 7. What Is `app.py`?

`app.py` is the main Python file of the project.

It contains:

* Flask application
* Routes
* API request logic
* API-key loading
* NewsAPI integration
* JSON processing
* Error handling

---

# 8. What Is `.env`?

`.env` means **environment file**.

It is used to store configuration values and secret information separately from the main source code.

For this project, the NewsAPI key is stored in `.env`.

Example:

```text
NEWS_API_KEY=YOUR_ACTUAL_API_KEY
```

The actual API key should be placed after `=`.

---

# 9. Why Did I Use `.env`?

I used `.env` to avoid directly writing my secret API key inside my Python source code.

For example, this is not recommended:

```python
API_KEY = "my-secret-api-key"
```

Instead, I use:

```python
API_KEY = os.getenv("NEWS_API_KEY")
```

The actual key remains outside the source code.

This makes it safer when the project is uploaded to GitHub.

---

# 10. What Is an Environment Variable?

An environment variable is a value stored outside the application's source code that the application can access while running.

In this project:

```text
NEWS_API_KEY
```

is the environment variable name.

Its value is the actual API key.

Conceptually:

```text
Environment Variable
        ↓
NEWS_API_KEY
        ↓
Actual API Key
```

---

# 11. How Does Python Read the `.env` File?

We install:

```bash
pip install python-dotenv
```

Then:

```python
from dotenv import load_dotenv
```

and:

```python
load_dotenv()
```

This loads the variables from `.env`.

Then:

```python
API_KEY = os.getenv("NEWS_API_KEY")
```

reads the API key.

The flow is:

```text
.env
 ↓
load_dotenv()
 ↓
Environment Variable
 ↓
os.getenv()
 ↓
Python gets API Key
```

---

# 12. What Is `.gitignore`?

`.gitignore` is a Git configuration file that tells Git which files or folders should **not be included in commits**.

Example:

```text
venv/
__pycache__/
*.pyc
.env
```

---

# 13. Why Did I Put `.env` in `.gitignore`?

I put `.env` inside `.gitignore` because it contains my secret API key.

If I upload `.env` to GitHub, another person could potentially see and use my API key.

Therefore:

```text
.env
```

is added to:

```text
.gitignore
```

The important idea is:

```text
Actual API Key
      ↓
     .env
      ↓
.gitignore
      ↓
Not uploaded to GitHub
```

---

# 14. Why Are `venv/` and `__pycache__/` in `.gitignore`?

### `venv/`

`venv` contains the local Python virtual environment and installed packages.

It is usually not necessary to upload the entire virtual environment to GitHub.

Instead, we use:

```text
requirements.txt
```

to tell others which packages are required.

### `__pycache__/`

Python creates this folder for cached Python bytecode.

It is generated automatically and does not need to be stored in GitHub.

---

# 15. What Is `requirements.txt`?

`requirements.txt` contains the Python packages required to run the project.

Example:

```text
Flask
requests
python-dotenv
```

When deploying or setting up the project on another computer:

```bash
pip install -r requirements.txt
```

installs the required packages.

---

# 16. How Did I Get the API?

I first identified that I needed a service that could provide news articles.

Then I searched for a suitable news API and referred to the **official NewsAPI documentation**.

I checked:

* Available endpoints
* HTTP method
* Required parameters
* Authentication requirements
* Response format

After understanding the documentation, I selected the appropriate endpoint and integrated it into my Flask application.

---

# 17. How Did I Obtain the API Key?

I obtained the API key from the NewsAPI provider.

The general process was:

```text
NewsAPI website
      ↓
Create account
      ↓
Sign in / verify account if required
      ↓
Access API key
      ↓
Copy the API key
      ↓
Store it in .env
```

I did not create the API key myself through Python.

The API provider generated/provided the key for my application/account.

---

# 18. Where Did You Store the API Key?

I stored it in the `.env` file.

Example:

```text
NEWS_API_KEY=MY_ACTUAL_KEY
```

I did not hard-code the actual key into `app.py`.

---

# 19. How Does the API Key Reach the API Request?

The process is:

```python
load_dotenv()

API_KEY = os.getenv("NEWS_API_KEY")
```

Then:

```python
params = {
    "q": topic,
    "language": "en",
    "sortBy": "publishedAt",
    "pageSize": 10,
    "apiKey": API_KEY
}
```

Then:

```python
response = requests.get(
    NEWS_API_URL,
    params=params
)
```

So:

```text
.env
 ↓
Python
 ↓
API_KEY
 ↓
requests.get()
 ↓
NewsAPI
```

---

# 20. What Is the NewsAPI Endpoint?

The application uses the NewsAPI `everything` endpoint:

```text
https://newsapi.org/v2/everything
```

The endpoint is used to search for news articles based on parameters.

For example, conceptually:

```text
endpoint
   +
q=Python
   +
language=en
   +
apiKey=YOUR_KEY
```

creates the API request.

---

# 21. What Is the `q` Parameter?

`q` represents the search query.

For example:

```text
q=Python
```

means:

> Search for news related to Python.

If the user enters:

```text
Artificial Intelligence
```

the backend sends that value as the search query.

---

# 22. What Is the API Key?

An API key is a credential provided by an API provider.

It is used to identify or authenticate the application making the API request.

Simple example:

```text
API
 ↓
"Who is making this request?"
 ↓
API Key
 ↓
"Here is the application's credential."
```

The API key is **not the API itself**.

```text
NewsAPI
   ↓
The API/service

API Key
   ↓
Credential used to access it
```

---

# 23. API vs API Key

| API                         | API Key                                |
| --------------------------- | -------------------------------------- |
| Provides functionality/data | Identifies/authenticates the requester |
| Example: NewsAPI            | Example: `NEWS_API_KEY`                |
| Has endpoints               | Is a credential                        |
| Receives requests           | Sent with the request                  |

---

# 24. Complete Project Architecture

```text
                    USER
                      |
                      ↓
             HTML / CSS / JavaScript
                      |
                      ↓
              Flask Backend
                      |
                      ↓
              Read .env file
                      |
                      ↓
                 API Key
                      |
                      ↓
             Python requests
                      |
                      ↓
                 NewsAPI
                      |
                      ↓
                JSON Response
                      |
                      ↓
             Flask processes data
                      |
                      ↓
                JSON Response
                      |
                      ↓
               JavaScript
                      |
                      ↓
                 NEWS CARDS
                      |
                      ↓
                    USER
```

---

# 25. Complete Request Flow

Suppose the user enters:

```text
Python
```

### Step 1

Frontend sends:

```text
/news?topic=Python
```

to Flask.

### Step 2

Flask gets:

```python
topic = request.args.get("topic")
```

### Step 3

Flask reads the API key:

```python
API_KEY = os.getenv("NEWS_API_KEY")
```

### Step 4

Flask creates parameters:

```python
params = {
    "q": topic,
    "language": "en",
    "sortBy": "publishedAt",
    "pageSize": 10,
    "apiKey": API_KEY
}
```

### Step 5

Python sends a GET request:

```python
requests.get(NEWS_API_URL, params=params)
```

### Step 6

NewsAPI validates the request and returns JSON.

### Step 7

Flask processes the JSON.

### Step 8

Flask sends the required article information to JavaScript.

### Step 9

JavaScript displays the articles.

---

# 26. What Is JSON?

JSON stands for **JavaScript Object Notation**.

It is a common format for exchanging structured data between applications.

Example:

```json
{
    "title": "Python Programming",
    "source": "Example News",
    "url": "https://example.com"
}
```

The API returns data in JSON format, and Python reads the JSON response.

---

# 27. Why Did You Use `requests`?

I used Python's `requests` library to send HTTP requests to the external NewsAPI.

For example:

```python
requests.get(
    NEWS_API_URL,
    params=params
)
```

It allows my Flask backend to communicate with the external API.

---

# 28. Why Did You Use Flask?

I used Flask because it is a lightweight Python web framework.

It allows me to:

* Create routes
* Receive requests
* Process user input
* Call external APIs
* Return JSON responses
* Connect frontend and backend

---

# 29. Why Didn't You Call NewsAPI Directly From JavaScript?

I used the Flask backend so that the API key is not exposed in frontend JavaScript.

The safer architecture is:

```text
Frontend
   ↓
Flask Backend
   ↓
API Key
   ↓
NewsAPI
```

rather than putting the secret API key directly into browser-side JavaScript.

---

# 30. What Is API Authentication?

Authentication is the process of verifying or identifying who is making a request.

In this project, the API key is used as the credential for accessing NewsAPI.

---

# 31. What Happens If the API Key Is Wrong?

The API provider can reject the request.

The application checks the response and returns an appropriate error message instead of assuming that every request succeeds.

---

# 32. What Happens If the User Doesn't Enter a Topic?

The backend checks:

```python
if not topic:
```

and returns:

```json
{
    "error": "Please enter a topic"
}
```

with an HTTP `400` status.

---

# 33. What Happens If the News API Is Unavailable?

The application catches request-related errors:

```python
except requests.exceptions.RequestException:
```

and returns an error response.

This prevents the application from crashing without handling the problem.

---

# 34. What HTTP Method Did You Use?

I used the **GET** method because I am retrieving news data from the external API.

```text
GET → Retrieve data
```

---

# 35. Is NewsAPI a REST API?

Yes. NewsAPI provides HTTP-based API endpoints that can be consumed using HTTP requests and returns structured data such as JSON.

In the project, I use a GET request to retrieve news articles.

---

# 36. Did You Create NewsAPI?

No.

NewsAPI is an external third-party service.

I integrated its API into my Flask application.

A good interview answer is:

> “No, I did not create the NewsAPI. I used it as a third-party API and integrated its endpoint into my Flask backend.”

---

# 37. Did You Create an API in This Project?

Yes.

I created a Flask endpoint:

```text
/news
```

The endpoint receives the user's topic, calls the external NewsAPI, processes its response, and returns the required data to the frontend.

So there are two API sides:

```text
My Flask API
      ↓
/news

External API
      ↓
NewsAPI
```

---

# 38. What Is the Difference Between Your Flask API and NewsAPI?

| My Flask API        | NewsAPI                         |
| ------------------- | ------------------------------- |
| Created by me       | Created by third-party provider |
| Built using Flask   | External service                |
| `/news` endpoint    | `/v2/everything` endpoint       |
| Receives user topic | Provides news data              |
| Calls NewsAPI       | Returns news information        |

---

# 39. Why Did You Use an External API Instead of Creating Your Own News Database?

Creating and maintaining a complete news database would require collecting, storing, updating, and managing news articles.

For a learning project, using an external API allowed me to focus on understanding:

* API integration
* Authentication
* Requests
* JSON
* Backend processing
* Frontend display

---

# 40. How Did You Know Which Parameters to Send?

I referred to the official API documentation.

The documentation explains:

* Endpoint
* HTTP method
* Required parameters
* Optional parameters
* Authentication
* Response structure

I used those documented details to construct my request.

---

# 41. How Did You Know Which Fields to Extract?

I checked the API documentation and its example JSON response.

From the response, I identified fields such as:

```text
title
description
source
url
urlToImage
```

Then I extracted only the fields needed by my application.

---

# 42. What Is an Endpoint?

An endpoint is a specific URL through which an application can access a particular API function or resource.

For this project:

```text
https://newsapi.org/v2/everything
```

is the external endpoint used to search for articles.

My Flask application also has:

```text
/news
```

as one of its endpoints.

---

# 43. What Is a Query Parameter?

A query parameter is additional information sent in the URL/request to control what data the API should return.

For example:

```text
q=Python
```

means the search query is Python.

In Flask:

```python
request.args.get("topic")
```

gets the query parameter sent by the frontend.

---

# 44. What Is the Difference Between `.env` and `.gitignore`?

This is an important interview question.

### `.env`

Stores secret/configuration values.

Example:

```text
NEWS_API_KEY=MY_SECRET_KEY
```

### `.gitignore`

Tells Git which files should not be tracked or uploaded.

Example:

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
Prevents .env from being committed
```

They have different purposes.

---

# 45. Is `.gitignore` Itself Secret?

No.

`.gitignore` does not contain the API key.

It only contains rules telling Git which files to ignore.

For example:

```text
.env
venv/
__pycache__/
```

---

# 46. What If You Accidentally Upload the API Key to GitHub?

I would immediately revoke or regenerate the exposed API key through the API provider and replace it with a new key.

Then I would remove the secret from the repository and make sure the `.env` file is ignored.

The important point is that simply deleting the key from the latest file may not remove it from Git history.

---

# 47. Why Should API Keys Not Be Hard-Coded?

Suppose I write:

```python
API_KEY = "abc123"
```

If I upload the source code to GitHub, the key could become visible to others.

Using:

```python
API_KEY = os.getenv("NEWS_API_KEY")
```

keeps the secret outside the source code.

---

# 48. How Would You Handle the API Key During Deployment?

During deployment, I would add the API key as an **environment variable/secret** in the hosting platform rather than uploading `.env` to GitHub.

The application can then read:

```python
os.getenv("NEWS_API_KEY")
```

without putting the actual key into the source code.

---

# 49. Why Did You Use `python-dotenv`?

I used `python-dotenv` to load variables from the local `.env` file into the application's environment.

This makes local development easier while keeping the secret separate from the source code.

---

# 50. What Did You Learn From This Project?

The main things I learned were:

1. API discovery
2. API documentation
3. API endpoints
4. HTTP GET requests
5. Query parameters
6. API keys
7. Authentication
8. Environment variables
9. `.env`
10. `.gitignore`
11. JSON responses
12. Flask routes
13. Frontend-backend communication
14. Third-party API integration
15. Error handling
16. Secure handling of credentials

---

# 51. What Was the Most Important Concept You Learned?

The most important concept I learned was **secure third-party API integration**.

Earlier, I understood how to call a public API.

With this project, I learned that when an API requires authentication, I should obtain the API key from the provider, store it securely, and use it from the backend instead of exposing it in frontend code.

---

# 52. One-Minute Project Explanation

> “I developed a News Search application using Python Flask, HTML, CSS, and JavaScript. The main purpose of the project was to learn third-party API integration with API-key-based authentication. The user enters a topic on the frontend, and JavaScript sends the topic to my Flask backend. The backend reads the NewsAPI key from an environment variable and sends a GET request to the NewsAPI endpoint along with the search parameters. NewsAPI returns the news information in JSON format. Flask processes the JSON response and sends the required article details back to the frontend, where they are displayed to the user. I stored the API key in a `.env` file and added `.env` to `.gitignore` so that the secret would not be committed to GitHub. Through this project, I learned API keys, authentication, REST APIs, JSON, query parameters, Flask, environment variables, and secure API integration.”

---

# 53. Short Interview Explanation

> “I built a News Search App using Flask and NewsAPI to learn API-key-based integration. The frontend sends the search topic to Flask, Flask reads the API key from an environment variable, calls the NewsAPI using a GET request, processes the JSON response, and sends the required news information back to the frontend. I used `.env` to store the API key and `.gitignore` to prevent the `.env` file from being committed to GitHub.”

---

# 54. Important Interview Questions — Quick List

### Project Basics

1. What is your project?
2. Why did you build this project?
3. What problem does it solve?
4. What are the main features?
5. What technologies did you use?
6. What was your role in the project?
7. Explain the project architecture.
8. Explain the complete project flow.
9. What did you learn from this project?

### API Questions

10. What is an API?
11. What is a REST API?
12. What is an endpoint?
13. What is an API request?
14. What is an API response?
15. What is JSON?
16. What is a query parameter?
17. What HTTP method did you use?
18. Why did you use GET?
19. How did you find the API?
20. How did you read the API documentation?
21. How did you know the endpoint?
22. How did you know which parameters to send?
23. How did you know which response fields to extract?

### API Key Questions

24. What is an API key?
25. Why does an API require an API key?
26. How did you obtain the API key?
27. Where did you store the API key?
28. Why didn't you hard-code the API key?
29. What is `.env`?
30. What is an environment variable?
31. How does Python read the API key?
32. Why did you use `python-dotenv`?
33. Why shouldn't the API key be stored in frontend JavaScript?
34. What happens if the API key is invalid?
35. What happens if your API key is exposed?
36. How would you handle the API key during deployment?

### Git/GitHub Questions

37. What is `.gitignore`?
38. Why did you add `.env` to `.gitignore`?
39. Why did you add `venv/` to `.gitignore`?
40. Why did you add `__pycache__/`?
41. Is `.gitignore` secret?
42. What happens if you accidentally push the API key to GitHub?
43. How would you secure the API key after deployment?

### Flask Questions

44. Why did you use Flask?
45. What is a Flask route?
46. What is `/news`?
47. How does Flask receive the user's topic?
48. What does `request.args.get()` do?
49. Why did you use `jsonify()`?
50. How does Flask communicate with NewsAPI?
51. How does Flask communicate with the frontend?

### Error Handling

52. What happens if the user enters nothing?
53. What happens if NewsAPI is unavailable?
54. What happens if the API key is invalid?
55. What HTTP status code do you return for bad input?
56. Why did you use `try-except`?
57. How do you handle API errors?

### Practical/Scenario Questions

58. What would happen if you removed `.env`?
59. What happens if `NEWS_API_KEY` is not found?
60. What happens if NewsAPI changes its response format?
61. How would you add categories to the application?
62. How would you add pagination?
63. How would you add a loading indicator?
64. How would you improve the UI?
65. How would you deploy the application?
66. How would you protect the API key in production?
67. How would you add another external API?
68. How would you store news articles in a database?
69. How would you add user authentication?
70. How would you make the application production-ready?

---

# 55. Best Answers to the Most Important Questions

### Q1. Why did you build this project?

> “I built this project mainly to learn third-party API integration with API-key-based authentication. I wanted to understand how to obtain an API key, securely store it, send authenticated requests from Flask, process JSON responses, and display the data in a frontend.”

### Q2. How did you get the API?

> “I first identified that I needed a news service. I searched for a suitable news API and referred to its official documentation. I checked the available endpoints, parameters, authentication requirements, and response format, and then integrated the required endpoint into my Flask application.”

### Q3. How did you obtain the API key?

> “I created an account with the API provider and obtained the API key provided for my application. I then stored it in a `.env` file instead of hard-coding it in my source code.”

### Q4. Why did you use `.env`?

> “I used `.env` to keep the API key separate from my source code. This reduces the chance of accidentally exposing the key when sharing or uploading the project.”

### Q5. Why did you use `.gitignore`?

> “I added `.env` to `.gitignore` so Git would not track and commit the file containing my API key. I also ignored generated files such as the virtual environment and Python cache files.”

### Q6. What if I remove `.gitignore`?

> “Git could potentially track the `.env` file when I add files using `git add .`. That could lead to accidentally committing the API key.”

### Q7. Did `.gitignore` remove the API key?

> “No. `.gitignore` only tells Git not to track certain files. It does not delete or encrypt the file.”

### Q8. Why didn't you put the API key in JavaScript?

> “Because JavaScript runs in the user's browser. A secret placed there can potentially be viewed by the user. I kept the API key on the Flask backend and made the backend call the external API.”

### Q9. Did you create NewsAPI?

> “No. NewsAPI is an external third-party service. I integrated its API into my Flask application.”

### Q10. What did you create?

> “I created the Flask backend and its `/news` endpoint. That endpoint receives the user's topic, calls the external NewsAPI, processes the response, and returns the required data to the frontend.”

### Q11. What happens when a user searches for Python?

> “The frontend sends `Python` to my Flask `/news` endpoint. Flask reads the API key from the environment, sends a GET request to NewsAPI with the search query and API key, receives the JSON response, extracts the required article information, and returns it to the frontend for display.”

### Q12. What if the API key is leaked?

> “I would revoke or regenerate the exposed key through the API provider and replace it with a new secret. I would also make sure the key is removed from the repository and that `.env` is properly ignored.”

---

# 56. Final Project Flow to Remember

```text
USER
  ↓
Enter News Topic
  ↓
HTML + JavaScript
  ↓
GET /news?topic=Python
  ↓
FLASK
  ↓
Read API Key
  ↓
.env → os.getenv()
  ↓
Python requests
  ↓
NewsAPI
  ↓
API Key Authentication
  ↓
JSON Response
  ↓
Flask Processes JSON
  ↓
JSON Response
  ↓
JavaScript
  ↓
Display News
  ↓
USER
```

---

# 57. Most Important Things to Remember for the Interview

```text
API
→ Lets applications communicate.

REST API
→ A common HTTP-based style of building web APIs.

Endpoint
→ Specific API URL.

API Key
→ Credential used by the API provider to identify/authenticate requests.

.env
→ Stores local secret/configuration values.

Environment Variable
→ Value available to the application outside the source code.

.gitignore
→ Tells Git which files should not be tracked.

requests
→ Python library used to send HTTP requests.

Flask
→ Python web framework used for the backend.

JSON
→ Common format used for exchanging structured data.

GET
→ HTTP method used here to retrieve news.

NewsAPI
→ External third-party API providing news data.
```

# 58. One-Line Memory Formula

```text
Find API
   ↓
Read Documentation
   ↓
Get API Key
   ↓
Store Key Securely
   ↓
Send GET Request
   ↓
Receive JSON
   ↓
Process JSON
   ↓
Display Data
```

This is the complete learning cycle for **API-key-based integration with Flask**.
