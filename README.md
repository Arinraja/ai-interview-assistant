# AI Interview Assistant (FastAPI)

##  Overview

AI Interview Assistant is a backend application that simulates a technical interview process. It generates role-based interview questions and evaluates user responses using a rule-based scoring system.

This project demonstrates backend API development and foundational AI evaluation logic.

---

##  Features

* Generate interview questions based on job role
* Evaluate answers with a score (0–100)
* Provide feedback for each answer
* Suggest improvements
* Modular and clean backend architecture

---

##  Tech Stack

* Python
* FastAPI
* Uvicorn
* Pydantic

---

##  Project Structure

```
ai-interview-assistant/
│
├── app/
│   ├── main.py
│   ├── question_generator.py
│   ├── answer_evaluator.py
│
├── requirements.txt
└── README.md
```

---

## How to Run Locally

### 1. Clone the Repository

```bash
git clone https://github.com/<your-username>/ai-interview-assistant.git
cd ai-interview-assistant
```

### 2. Create Virtual Environment

```bash
python -m venv venv
```

Activate:

```bash
venv\Scripts\activate   # Windows
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the Server

```bash
uvicorn app.main:app --reload
```

### 5. Open in Browser

```
http://127.0.0.1:8000/docs
```

 Use Swagger UI to test APIs interactively.

---

## API Endpoints

###  Generate Questions

**POST** `/generate-questions/`

Request:

```json
{
  "role": "Python Developer"
}
```

Response:

```json
{
  "questions": [
    "What is Python?",
    "Explain list vs tuple."
  ]
}
```

---

###  Evaluate Answers

**POST** `/evaluate-answers/`

Request:

```json
{
  "questions": ["What is Python?"],
  "answers": ["Python is a programming language used for web and data science."]
}
```

Response:

```json
{
  "final_score": 85,
  "details": [...],
  "suggestions": [...]
}
```

---

##  How It Works

### Question Generation

* Uses rule-based logic
* Matches keywords from job roles

### Answer Evaluation

* Relevance → keyword matching
* Completeness → answer length
* Technical correctness → keyword presence

---

##  Why This Project Matters (For Recruiters)

This project demonstrates:

* REST API development using FastAPI
* Clean and modular backend design
* Input validation using Pydantic
* Basic AI evaluation logic
* Ability to build scalable backend systems

---

##  Future Improvements

* LLM-based evaluation (OpenAI integration)
* Database integration (store responses)
* Frontend UI (React)
* Authentication system
* Advanced NLP scoring

---



##  Quick Start

1. Run the server
2. Open `/docs`
3. Generate questions
4. Submit answers
5. Get feedback and score

---
