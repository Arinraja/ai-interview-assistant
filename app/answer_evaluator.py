def evaluate_answers(questions, answers):
    total_score = 0
    feedback_list = []

    for q, a in zip(questions, answers):
        score = 0
        feedback = []

        # Relevance (basic check)
        if any(word in a.lower() for word in q.lower().split()):
            score += 30
        else:
            feedback.append("Answer may not be relevant.")

        # Completeness (length check)
        if len(a.split()) > 20:
            score += 30
        else:
            feedback.append("Answer is too short.")

        # Technical correctness (basic keywords)
        if "python" in a.lower() or "data" in a.lower():
            score += 40
        else:
            feedback.append("Lacks technical depth.")

        total_score += score

        feedback_list.append({
            "question": q,
            "score": score,
            "feedback": feedback
        })

    final_score = total_score / len(questions)

    return {
        "final_score": round(final_score, 2),
        "details": feedback_list,
        "suggestions": [
            "Provide more detailed answers.",
            "Use technical keywords.",
            "Structure answers clearly."
        ]
    }
