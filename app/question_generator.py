def generate_questions(role: str):
    role = role.lower()

    if "python" in role:
        return [
            "What is Python?",
            "Explain list vs tuple.",
            "What is OOP in Python?",
            "Explain decorators.",
            "What is exception handling?"
        ]

    elif "data scientist" in role:
        return [
            "What is machine learning?",
            "Explain supervised vs unsupervised learning.",
            "What is overfitting?",
            "Explain regression.",
            "What is a confusion matrix?"
        ]

    else:
        return [
            f"What skills are required for a {role}?",
            f"Explain a project you would do as a {role}.",
            f"What tools are used in {role}?",
            f"What challenges are faced in {role}?",
            f"What is your learning roadmap for {role}?"
        ]
