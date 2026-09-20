# from backend.rag.embedder import create_embedding
# from backend.rag.vector_store import collection
# from backend.rag.generator import generate_answer


# DISTANCE_THRESHOLD = 0.5


# def answer_question(question, top_k=3):

#     # 1. Convert question into an embedding
#     question_embedding = create_embedding(question)

#     # 2. Retrieve Top-K candidates
#     results = collection.query(
#         query_embeddings=[question_embedding.tolist()],
#         n_results=top_k
#     )

#     documents = results["documents"][0]
#     distances = results["distances"][0]
#     metadatas = results["metadatas"][0]

#     # 3. Keep only sufficiently similar chunks
#     filtered_chunks = []

#     print("\n--- RETRIEVED CHUNKS ---")

#     for i in range(len(documents)):

#         print(f"\nChunk {i + 1}")
#         print("Distance:", distances[i])
#         print("Metadata:", metadatas[i])
#         print("Text:")
#         print(documents[i])

#         if distances[i] < DISTANCE_THRESHOLD:
#             filtered_chunks.append(documents[i])

#     # 4. No sufficiently relevant context
#     if not filtered_chunks:
#         return "I could not find the answer in the provided document."

#     # 5. Build context from relevant chunks
#     context = "\n\n".join(filtered_chunks)

#     # 6. Generate answer using Gemini
#     answer = generate_answer(question, context)

#     return answer

from backend.rag.embedder import create_embedding
from backend.rag.vector_store import collection
from backend.rag.generator import generate_answer


DISTANCE_THRESHOLD = 0.5


def retrieve_chunks(question, top_k=3):

    question_embedding = create_embedding(question)

    results = collection.query(
        query_embeddings=[question_embedding.tolist()],
        n_results=top_k
    )

    documents = results["documents"][0]
    distances = results["distances"][0]
    metadatas = results["metadatas"][0]

    relevant_chunks = []

    for i in range(len(documents)):

        if distances[i] < DISTANCE_THRESHOLD:
            relevant_chunks.append({
                "text": documents[i],
                "distance": distances[i],
                "metadata": metadatas[i]
            })

    return relevant_chunks


def answer_question(question, top_k=3):

    relevant_chunks = retrieve_chunks(question, top_k)

    context_parts = []

    for chunk in relevant_chunks:

        metadata = chunk["metadata"]

        context_parts.append(
            f"""
    [Source: {metadata['source']}, Page: {metadata['page_number']}]

    {chunk['text']}
    """
        )

    context = "\n\n".join(context_parts)

    return generate_answer(question, context)