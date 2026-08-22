from backend.rag.embedder import create_embedding
from backend.rag.vector_store import collection

question = "How many layers are there in the OSI model?"

# Create embedding for the question
question_embedding = create_embedding(question)

# Ask ChromaDB for the Top 3 similar chunks
results = collection.query(
    query_embeddings=[question_embedding.tolist()],
    n_results=3
)

print("\nQuestion:")
print(question)

print("\nTop 3 relevant chunks:\n")

for i in range(3):
    print("Chunk ID:", results["ids"][0][i])
    print("Chunk:")
    print(results["documents"][0][i])
    print("Metadata:", results["metadatas"][0][i])
    print("Distance:", results["distances"][0][i])
    print("-" * 50)