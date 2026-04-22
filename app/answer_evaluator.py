def evaluate_answers(questions, answers):
    total_score = 0
    feedback_list = []

    for q, a in zip(questions, answers):
        score = 0
        feedback = []

        a_clean = a.lower().strip()
        q_words = q.lower().split()

        #  Handle empty answer
        if not a_clean:
            feedback_list.append({
                "question": q,
                "score": 0,
                "feedback": ["No answer provided"]
            })
            continue

        #  1. Relevance (keyword overlap)
        match = sum(1 for word in q_words if word in a_clean)
        relevance_score = (match / len(q_words)) * 30
        relevance_score = min(relevance_score, 30)
        score += relevance_score

        if relevance_score < 10:
            feedback.append("Answer not aligned with question")

        #  2. Completeness (length-based)
        word_count = len(a_clean.split())
        length_score = min((word_count / 50) * 30, 30)
        score += length_score

        if word_count < 10:
            feedback.append("Answer too short")
        elif word_count > 80:
            feedback.append("Answer could be more concise")

        #  3. Technical depth (improved)
        tech_keywords = set(q_words)  # dynamic based on question
        tech_match = sum(1 for word in tech_keywords if word in a_clean)

        tech_score = min((tech_match / len(tech_keywords)) * 40, 40)
        score += tech_score

        if tech_score < 15:
            feedback.append("Add more technical details")

        #  Normalize score (0–100)
        score = min(score, 100)

        total_score += score

        feedback_list.append({
            "question": q,
            "score": round(score, 2),
            "feedback": feedback if feedback else ["Good answer"]
        })

    #  Avoid division error
    final_score = total_score / len(questions) if questions else 0

    return {
        "final_score": round(final_score, 2),
        "details": feedback_list,
        "suggestions": [
            "Use structured answers (intro, explanation, example)",
            "Include real-world examples",
            "Focus on clarity and technical accuracy"
        ]
    }
