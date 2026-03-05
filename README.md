# Text Analyzer

A simple web application that analyzes text and returns statistics such as word count, character count, sentence count, and the most frequent words.

The application consists of:
- **Backend:** FastAPI
- **Frontend:** Simple HTML + JavaScript
- **Containerization:** Docker & docker-compose

---

# Features

The application analyzes user-provided text and returns:

- Word count
- Character count (with spaces)
- Character count (without spaces)
- Sentence count
- Top 5 most frequent words (excluding stop words)

Text analysis rules:

- Words are counted **case-insensitively**
- Punctuation is **not considered part of words**
- Numbers count as words
- Contractions such as **don't** and **it's** count as a single word
- Sentence delimiters: `.`, `!`, `?`
- Ellipsis (`...`) counts as a **single sentence delimiter**

---
# Setup Instructions

### 1 Clone the repository

git clone <repository_url>
cd text_analyzer


### 2 Run the application with Docker
docker-compose up --build

### 3 Open the application

Frontend: http://localhost:3000  
Backend API: http://localhost:8000  

### 4 Running Tests

Run tests inside the backend container:
docker-compose exec backend python -m pytest


### Answers to Questions
1. What would you improve if you had more time?

If I had more time, I would:
    Improve sentence detection (handle abbreviations like "Mr." or "Dr.")
    Improve the frontend UI and add loading/error states
    Add CI (GitHub Actions) for automated testing

2. What problems could arise with a 1,000,000-character text?

Possible problems include:
    Increased memory usage
    Slower processing if inefficient algorithms are used

To address this:
    Ensure the algorithm runs in O(n) time
    Avoid repeated passes over the text

3. How would you scale the application to handle 1,000 concurrent users?

Possible approaches:
    Use async request handling (FastAPI already supports this)
    Add caching if repeated texts are analyzed


I confirm that I completed this task independently.
