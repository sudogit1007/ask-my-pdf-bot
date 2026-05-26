import os
from dotenv import load_dotenv
import google.generativeai as genai

print("CHATBOT FILE LOADED")

load_dotenv()

api_key = os.getenv("GOOGLE_API_KEY")

genai.configure(api_key=api_key)

model = genai.GenerativeModel("gemini-2.5-flash")


def ask_question(question, matches):

    context = ""

    for item in matches:
        context += f"Page {item['page']}:\n{item['text']}\n\n"

    prompt = f"""
You are a document assistant.

Answer ONLY using the PDF content below.

Rules:
- Do not guess
- Do not make things up
- If answer is missing, say "Not found in document"

PDF Content:
{context}

Question:
{question}
"""

    response = model.generate_content(prompt)

    pages = []

    for match in matches:
        if match["page"] not in pages:
            pages.append(match["page"])

    return response.text, pages