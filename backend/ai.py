import requests

# this is used to send requests to the Ollama API for generating responses based on prompts. The code defines several functions that interact with the Ollama API to answer questions, generate summaries, quizzes, and flashcards based on provided study material.

OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL_NAME = "qwen3:4b"
def ask_ollama(prompt):
    response = requests.post(
        OLLAMA_URL,
        json={
            "model": MODEL_NAME,
            "prompt": prompt,
            "stream": False
        },
        timeout=120
    )
    response.raise_for_status()
    data = response.json()
    return data["response"]


def answer_question(question, context):
    prompt = f"""
You are OpenStudy AI, a helpful study assistant.

Answer the student's question using the study material provided below.

IMPORTANT RULES:

1. Use the provided study material as the main source.
2. Do not invent information.
3. If the answer cannot be found in the material, clearly say:
   "I could not find this information in the uploaded document."
4. Explain difficult concepts in simple language.
5. Give examples when useful.
6. Keep the answer structured and easy to understand.

STUDY MATERIAL:
----------------
{context}
----------------

STUDENT QUESTION:
{question}

ANSWER:
"""

    return ask_ollama(prompt)


def generate_summary(context):
    prompt = f"""
You are OpenStudy AI.

Create a clear study summary from the following material.

Include:

1. Main concepts
2. Important definitions
3. Important points
4. Important formulas if present
5. Key things a student should remember

Use simple language.

STUDY MATERIAL:
{context}

SUMMARY:
"""

    return ask_ollama(prompt)


def generate_quiz(context):
    prompt = f"""
You are OpenStudy AI.

Create 5 multiple-choice questions from the following study material.

For each question provide:

Question
A
B
C
D
Correct Answer
Short Explanation

Only use information from the study material.

STUDY MATERIAL:
{context}

QUIZ:
"""

    return ask_ollama(prompt)


def generate_flashcards(context):
    prompt = f"""
You are OpenStudy AI.

Create 8 study flashcards from the following material.

Format each one as:

Question:
Answer:

Keep answers short and useful for revision.

STUDY MATERIAL:
{context}

FLASHCARDS:
"""

    return ask_ollama(prompt)