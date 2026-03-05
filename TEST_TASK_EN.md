# Test Assignment: Text Analyzer

**Position:** Full-Stack Python Developer
**Estimated time:** up to 3 hours
**Deadline:** 3 days from receipt

> This assignment does not require a perfect production-grade solution.
> We evaluate your approach, attention to detail, and ability to see a task through to completion.
> After submission, we will have a short call (15 minutes) where we'll ask you to walk us through your solution.

---

## Task

Build a web application called **"Text Analyzer"** — a user enters text, and the application analyzes it and returns statistics.

---

## Functionality

The user enters text into an input field and clicks the **"Analyze"** button.

The server should return:

- Word count
- Character count (with and without spaces)
- Sentence count
- Top 5 most frequent words (**excluding stop words**: the, a, an, is, are, was, were, in, on, at, to, and, or, but, of, for, with, not, it, this, that)

### Word Counting Rules

- Words are counted **case-insensitively** (`Hello` and `hello` are the same word)
- Punctuation is **not part of** a word (`word.` → `word`, `"hello"` → `hello`)
- Numbers count as words (`42` is a word)
- Contractions with apostrophes count as a single word (`it's` — one word, `don't` — one word)

### Sentence Counting Rules

- Sentence delimiters: `.` `!` `?`
- An ellipsis (`...`) counts as **one** delimiter (not three sentences)
- Text without any delimiters is 1 sentence

### Constraints

- The application must correctly handle texts **up to 100,000 characters**
- Production-grade optimization is not required — a reasonable implementation without obvious inefficiencies is sufficient (e.g., avoid O(n²) where O(n) is possible)

### Library Restrictions

- Using third-party text analysis libraries (e.g., `nltk`, `spacy`, `textblob`) is **not allowed**
- The analysis logic must be implemented by you
- Python standard library modules (`re`, `collections`, etc.) are allowed

---

## Backend

- **Python** (FastAPI, Flask, or Django — your choice)
- One POST endpoint: `/analyze`

**Request:**

```json
{
  "text": "Some example text. Another sentence!"
}
```

**Response:**

```json
{
  "word_count": 6,
  "char_count_with_spaces": 36,
  "char_count_without_spaces": 31,
  "sentence_count": 2,
  "top_words": [
    { "word": "some", "count": 1 },
    { "word": "example", "count": 1 },
    { "word": "text", "count": 1 },
    { "word": "another", "count": 1 },
    { "word": "sentence", "count": 1 }
  ]
}
```

### Sample Input for Self-Testing

Use this text to verify your solution:

**Input text:**

```
The quick brown fox jumps over the lazy dog. The dog barked, but the fox kept running!

Fox and dog... they're actually friends. The fox visits the dog every day, and the dog always welcomes the fox. It's a beautiful friendship.

Don't you love stories about animals? Animals bring joy and happiness. The fox and the dog are proof that friendship has no boundaries!
```

**Expected API response:**

```json
{
  "word_count": 64,
  "char_count_with_spaces": 365,
  "char_count_without_spaces": 300,
  "sentence_count": 9,
  "top_words": [
    { "word": "fox", "count": 6 },
    { "word": "dog", "count": 6 },
    { "word": "friendship", "count": 2 },
    { "word": "animals", "count": 2 },
    { "word": "quick", "count": 1 }
  ]
}
```

> **Note:** `fox` and `dog` have equal frequency — their order may vary.
> The 5th word in `top_words` can be any word with a count of 1 (many are tied).

---

## Frontend

A simple HTML page with:

- A `textarea` for text input
- An **"Analyze"** button
- A results display area

You may use:

- Plain HTML / CSS / JS
- Or React / Vue (optional)

> **UI styling is not evaluated.** The frontend can be minimal — what matters is that it works and is understandable.

---

## Requirements

### Mandatory

1. Code is well-structured (backend and frontend are logically separated)
2. Edge case handling:
   - Empty text
   - Single-word text
   - Text with line breaks
3. Basic error handling (invalid JSON, missing `text` field)
4. **2–3 unit tests** for the core text analysis logic
5. **README** with setup instructions (see below)
6. The project must run locally

### Nice to Have (not required)

- Docker / docker-compose
- Additional tests
- Linter / formatter

---

## README

Your README.md should contain:

1. **Brief description** of the project
2. **Setup instructions** (step by step, from cloning to opening in browser)
3. **Answers to the questions** (see below)

### Questions (must be answered in writing in the README)

1. What would you improve if you had more time?
2. What problems could arise when processing a 1,000,000-character text? How would you address them?
3. How would you scale this application to handle 1,000 concurrent users?

At the end of your README, please include this line:

> `I confirm that I completed this task independently.`

---

## What to Submit

- A link to a **GitHub repository** (preferred)
- Or a project archive

> We pay attention to commit history. A single "initial commit" is a negative signal.
> Make commits as you work, as you would on a real project.

---

## Evaluation Criteria

| Criterion | Weight |
|---|---|
| Project runs following README instructions | 20% |
| Project structure | 15% |
| Correctness of text analysis | 15% |
| Error handling and edge cases | 10% |
| Tests | 10% |
| Frontend (functional, understandable) | 10% |
| README quality | 10% |
| Answers to questions | 10% |

---

## After Submission

We will schedule a **short call (15 minutes)** where we'll ask you to:

- Walk us through your project and explain your decisions
- Answer a few questions about the code
- Make a small change live

This is a standard part of our process — no special preparation is needed, just understand your own code.

---

*Good luck! If you have any questions about the assignment, please ask before you start.*
