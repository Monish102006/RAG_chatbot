from backend.rag.vector_store import client

client.delete_collection("pdf_chunks")

print("Vector store reset successfully.")