def create_rag_prompt(question, context):
    prompt = f"""
You are a helpful assistant answering questions based on the provided context.

CONTEXT:
{context}

QUESTION:
{question}

Answer the question using only the information provided in the context.
If the answer cannot be found in the context, say:
"I could not find the answer in the provided document."
"""

    return prompt