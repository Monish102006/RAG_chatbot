# import chromadb

# # Create a persistent Chroma client
# client = chromadb.PersistentClient(
#     path="data/chroma_db"
# )

# # Create or get our collection
# collection = client.get_or_create_collection(
#     name="pdf_chunks"
# )

import chromadb

client = chromadb.PersistentClient(
    path="data/chroma_db"
)

collection = client.get_or_create_collection(
    name="pdf_chunks",
    configuration={
        "hnsw": {
            "space": "cosine"
        }
    }
)