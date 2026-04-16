from fastapi import FastAPI
from pydantic import BaseModel
from app.question_generator import generate_questions
from app.answer_evaluator import evaluate_answers

app = FastAPI()

# Request Models
class RoleRequest(BaseModel):
    role: str

class AnswerRequest(BaseModel):
    questions: list[str]
    answers: list[str]

# API 1: Generate Questions
@app.post("/generate-questions/")
def get_questions(request: RoleRequest):

    
    questions = generate_questions(request.role)
    return {"questions": questions}

# API 2: Evaluate Answers
@app.post("/evaluate-answers/")
def evaluate(request: AnswerRequest):
    result = evaluate_answers(request.questions, request.answers)
    return result
