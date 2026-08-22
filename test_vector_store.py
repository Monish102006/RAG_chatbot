from backend.rag.vector_store import collection

print("Collection name:", collection.name)
print("Number of items:", collection.count())
print("Metadata:", collection.metadata)