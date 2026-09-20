from backend.rag.rag_pipeline import retrieve_chunks


questions = [
    "How many layers are there in the OSI model?",
    "What is the primary function of the Physical Layer?",
    "What does the Network Layer do?",
    "What is the purpose of the Transport Layer?",
    "What is the capital of France?"
]


for question in questions:

    print("\n" + "=" * 70)
    print("QUESTION:", question)
    print("=" * 70)

    chunks = retrieve_chunks(question)

    if not chunks:
        print("NO RELEVANT CHUNKS FOUND")
        continue

    for i, chunk in enumerate(chunks, start=1):

        print(f"\nResult {i}")
        print("Distance:", round(chunk["distance"], 4))
        print("Page:", chunk["metadata"]["page_number"])
        print("Text:", chunk["text"][:300])