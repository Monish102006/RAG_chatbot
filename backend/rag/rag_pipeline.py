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


def answer_question_with_sources(question, top_k=3):

    relevant_chunks = retrieve_chunks(question, top_k)

    if not relevant_chunks:

        return {
            "answer": "I could not find the answer in the provided document.",
            "sources": []
        }

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

    answer = generate_answer(question, context)

    sources = []

    for chunk in relevant_chunks:

        metadata = chunk["metadata"]

        source = {
            "source": metadata["source"],
            "page": metadata["page_number"]
        }

        if source not in sources:
            sources.append(source)

    return {
        "answer": answer,
        "sources": sources
    }


def answer_question(question, top_k=3):

    result = answer_question_with_sources(question, top_k)

    return result["answer"]