import os
import json
from openai import OpenAI
from dotenv import load_dotenv

print("🔥 LLM SERVICE FILE LOADED 🔥")

load_dotenv()

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=os.getenv("OPENROUTER_API_KEY")
)


# ------------------ GENERATE QUESTIONS ------------------
def generate_questions_llm(role: str):
    try:
        prompt = f"""
        Generate 5 interview questions for {role}.

        RULES:
        - Return ONLY valid JSON
        - No explanation
        - No markdown
        - No extra text

        FORMAT:
        {{
          "questions": ["q1","q2","q3","q4","q5"]
        }}
        """

        response = client.chat.completions.create(
            model="meta-llama/llama-3-8b-instruct",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.7
        )

        text = response.choices[0].message.content
        print("RAW QUESTIONS:", text)

        return text

    except Exception as e:
        return json.dumps({"error": str(e)})


# ------------------ EVALUATE ANSWERS ------------------
def evaluate_answers_llm(data):
    try:
        prompt = f"""
        You are an AI interviewer.

        Evaluate the following answers.

        STRICT RULES:
        - Return ONLY valid JSON
        - No explanation
        - No code
        - No markdown
        - No extra text

        FORMAT:
        {{
          "score": number (0-100),
          "feedback": "short summary",
          "suggestions": ["point1","point2"]
        }}

        DATA:
        {data}
        """

        response = client.chat.completions.create(
            model="meta-llama/llama-3-8b-instruct",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.3
        )

        text = response.choices[0].message.content
        print("RAW EVALUATION:", text)

        return text

    except Exception as e:
        return json.dumps({"error": str(e)})
