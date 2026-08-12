from backend.services.pdf_service import extract_text_from_pdf
from backend.rag.chunker import chunk_text

pdf_path = "data/uploads/sample.pdf"

# Step 1: Extract text from PDF
text = extract_text_from_pdf(pdf_path)

print("Total text length:", len(text))

# Step 2: Split text into chunks
chunks = chunk_text(text)

print("Number of chunks:", len(chunks))

# Display the first chunk
print("\n--- Chunk 1 ---\n")
print(chunks[0])

print("\n--- Chunk 2 ---\n")
print(chunks[1])