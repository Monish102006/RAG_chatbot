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


# from backend.services.pdf_service import extract_pages_from_pdf
# from backend.rag.chunker import chunk_text
# from backend.rag.embedder import create_embedding
# from backend.rag.vector_store import collection
# from pathlib import Path

# PDF_PATH = "data/uploads/sample.pdf"

# document_id = Path(PDF_PATH).stem
# source = Path(PDF_PATH).name

# # Step 1: Extract pages
# pages = extract_pages_from_pdf(PDF_PATH)

# chunk_id = 0


# # Step 2: Process each page
# for page in pages:

#     page_number = page["page_number"]
#     page_text = page["text"]

#     # Create chunks for this page
#     chunks = chunk_text(page_text)

#     # Step 3: Store chunks in Chroma
#     for chunk_index, chunk in enumerate(chunks):

#         embedding = create_embedding(chunk)

#         collection.add(
#             ids=[f"chunk_{chunk_id}"],
#             documents=[chunk],
#             embeddings=[embedding.tolist()],
#             metadatas=[
#                 {
#                     "document_id": document_id,
#                     "source": "sample.pdf",
#                     "page_number": page_number,
#                     "chunk_index": chunk_index
#                 }
#             ]
#         )

#         chunk_id += 1


# print("Total chunks stored:", chunk_id)



from pathlib import Path

from backend.services.pdf_service import extract_pages_from_pdf
from backend.rag.chunker import chunk_text
from backend.rag.embedder import create_embedding
from backend.rag.vector_store import collection


PDF_DIRECTORY = Path("data/uploads")


def ingest_pdf(pdf_path):
    source = pdf_path.name
    document_id = pdf_path.stem

    print(f"\nProcessing: {source}")

    pages = extract_pages_from_pdf(pdf_path)

    total_chunks = 0

    for page in pages:
        page_number = page["page_number"]
        page_text = page["text"]

        chunks = chunk_text(page_text)

        for chunk_index, chunk in enumerate(chunks):

            chunk_id = f"{document_id}_p{page_number}_c{chunk_index}"

            embedding = create_embedding(chunk)

            metadata = {
                "document_id": document_id,
                "source": source,
                "page_number": page_number,
                "chunk_index": chunk_index
            }

            collection.upsert(
                ids=[chunk_id],
                documents=[chunk],
                embeddings=[embedding.tolist()],
                metadatas=[metadata]
            )

            total_chunks += 1

    print(f"Chunks stored from {source}: {total_chunks}")

    return total_chunks


def ingest_all_pdfs():
    pdf_files = list(PDF_DIRECTORY.glob("*.pdf"))

    if not pdf_files:
        print("No PDF files found.")
        return

    total_chunks = 0

    for pdf_path in pdf_files:
        total_chunks += ingest_pdf(pdf_path)

    print("\n" + "=" * 50)
    print(f"Total chunks stored: {total_chunks}")
    print("=" * 50)


if __name__ == "__main__":
    ingest_all_pdfs()