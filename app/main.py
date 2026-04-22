from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
from pydantic import BaseModel, Field
import json
import re

# 👉 LLM functions
from services.llm_service import generate_questions_llm, evaluate_answers_llm

app = FastAPI()

# -------------------- CORS --------------------
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# -------------------- MODELS --------------------
class RoleRequest(BaseModel):
    role: str = Field(..., min_length=3)

class AnswerRequest(BaseModel):
    questions: list[str]
    answers: list[str]

# -------------------- SAFE PARSE --------------------
def safe_parse(text: str):
    try:
        start = text.find("{")
        end = text.rfind("}") + 1

        if start == -1 or end == -1:
            return {"error": "No JSON found", "raw": text}

        json_text = text[start:end]
        return json.loads(json_text)

    except Exception:
        return {"error": "Invalid JSON from LLM", "raw": text}

# -------------------- ROOT --------------------
@app.get("/")
def home():
    return FileResponse("frontend/index.html")

# -------------------- GENERATE QUESTIONS --------------------
@app.post("/generate-questions/")
def generate_questions(role: str):
    try:
        raw_response = generate_questions_llm(role)
        return safe_parse(raw_response)

    except Exception as e:
        return {"error": str(e)}

# -------------------- EVALUATE ANSWERS --------------------
@app.post("/evaluate-answers/")
def evaluate_answers(data: dict):
    try:
        raw_response = evaluate_answers_llm(data)
        return safe_parse(raw_response)

    except Exception as e:
        return {"error": str(e)}
