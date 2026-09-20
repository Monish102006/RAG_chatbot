import os

from dotenv import load_dotenv
from google import genai

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)


def generate_answer(question, context):

    prompt = f"""
You are a RAG assistant.

Answer the question using the provided document context.

CONTEXT:
{context}

QUESTION:
{question}

Rules:
1. Use the provided context as the source of truth.
2. You may reason over information contained in the context.
3. Do not introduce unsupported information.
4. If the context does not contain enough information to answer the question,
   say:
"I could not find the answer in the provided document."
5. Give a concise and direct answer.
"""

    response = client.interactions.create(
        model="gemini-3.6-flash",
        input=prompt
    )

    return response.output_text