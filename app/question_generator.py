def generate_questions(role: str):
    role = role.lower().strip()

    role_questions = {
        "python": [
            "What is Python and its key features?",
            "Explain list vs tuple with examples.",
            "What is OOP in Python?",
            "Explain decorators in Python.",
            "What is exception handling?",
            "What are Python generators?",
            "Explain GIL in Python."
        ],

        "data scientist": [
            "What is machine learning?",
            "Explain supervised vs unsupervised learning.",
            "What is overfitting and how to prevent it?",
            "Explain regression vs classification.",
            "What is a confusion matrix?",
            "What is feature engineering?",
            "Explain cross-validation."
        ],

        "web developer": [
            "What is HTML, CSS, and JavaScript?",
            "Explain REST API.",
            "What is frontend vs backend?",
            "What is a framework?",
            "Explain HTTP methods.",
            "What is authentication?",
            "Explain MVC architecture."
        ]
    }

    #  Match role
    for key in role_questions:
        if key in role:
            return role_questions[key]

    # Default fallback (dynamic)
    return [
        f"What skills are required for a {role}?",
        f"Explain a real-world project for a {role}.",
        f"What tools and technologies are used in {role}?",
        f"What challenges are faced in {role}?",
        f"What is your roadmap to become a {role}?"
    ]
