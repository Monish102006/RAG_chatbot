# from backend.rag.rag_pipeline import retrieve_chunks


# question = "What is the time complexity of binary search?"

# chunks = retrieve_chunks(question)

# print("\nQUESTION:")
# print(question)

# print("\n--- FILTERED RETRIEVAL ---")

# for i, chunk in enumerate(chunks, start=1):

#     print(f"\nResult {i}")
#     print("Distance:", chunk["distance"])
#     print("Metadata:", chunk["metadata"])
#     print("Text:")
#     print(chunk["text"])

from backend.rag.rag_pipeline import retrieve_chunks


questions = [
    "What is the time complexity of binary search?",
    "What is the OSI model?"
]


for question in questions:

    print("\n" + "=" * 70)
    print("QUESTION:")
    print(question)
    print("=" * 70)

    chunks = retrieve_chunks(question)

    if not chunks:
        print("NO RELEVANT CHUNKS FOUND")
        continue

    for i, chunk in enumerate(chunks, start=1):

        print(f"\nResult {i}")
        print("Distance:", chunk["distance"])
        print("Source:", chunk["metadata"]["source"])
        print("Page:", chunk["metadata"]["page_number"])
        print("Text:")
        print(chunk["text"][:500])