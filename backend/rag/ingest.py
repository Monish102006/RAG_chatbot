# from backend.services.pdf_service import extract_text_from_pdf
# from backend.rag.chunker import chunk_text
# from backend.rag.embedder import create_embedding
# from backend.rag.vector_store import collection

# PDF_PATH = "data/uploads/sample.pdf"

# # Step 1: Extract text
# text = extract_text_from_pdf(PDF_PATH)

# # Step 2: Create chunks
# chunks = chunk_text(text)

# print("Number of chunks:", len(chunks))

# # Step 3: Store chunks in Chroma
# for i, chunk in enumerate(chunks):

#     embedding = create_embedding(chunk)

#     collection.add(
#         ids=[f"chunk_{i}"],
#         documents=[chunk],
#         embeddings=[embedding.tolist()],
#         metadatas=[
#             {
#                 "source": "sample.pdf",
#                 "chunk_index": i
#             }
#         ]
#     )

# print("Chunks successfully stored in Chroma!")


from backend.services.pdf_service import extract_pages_from_pdf
from backend.rag.chunker import chunk_text
from backend.rag.embedder import create_embedding
from backend.rag.vector_store import collection
from pathlib import Path

PDF_PATH = "data/uploads/sample.pdf"

document_id = Path(PDF_PATH).stem
source = Path(PDF_PATH).name

# Step 1: Extract pages
pages = extract_pages_from_pdf(PDF_PATH)

chunk_id = 0


# Step 2: Process each page
for page in pages:

    page_number = page["page_number"]
    page_text = page["text"]

    # Create chunks for this page
    chunks = chunk_text(page_text)

    # Step 3: Store chunks in Chroma
    for chunk_index, chunk in enumerate(chunks):

        embedding = create_embedding(chunk)

        collection.add(
            ids=[f"chunk_{chunk_id}"],
            documents=[chunk],
            embeddings=[embedding.tolist()],
            metadatas=[
                {
                    "document_id": document_id,
                    "source": "sample.pdf",
                    "page_number": page_number,
                    "chunk_index": chunk_index
                }
            ]
        )

        chunk_id += 1


print("Total chunks stored:", chunk_id)