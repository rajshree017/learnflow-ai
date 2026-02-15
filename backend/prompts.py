def tutor_prompt(topic, language):
    return f"""
Explain this topic in simple {language} with examples:

Topic: {topic}
"""


def roadmap_prompt(goal, days, language):
    return f"""
Create a {days}-day roadmap in {language} for:

Goal: {goal}

Include daily topics + practice tasks.
"""


def quiz_prompt(topic, language):
    return f"""
Generate 5 quiz questions in {language} on:

Topic: {topic}
"""


def debug_prompt(issue, language):
    return f"""
Fix this coding issue and explain in {language}:

{issue}
"""


def docs_prompt(code, language):
    return f"""
Generate documentation in {language} for this code:

{code}
"""
