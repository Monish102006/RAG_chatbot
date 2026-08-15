#tesing the embedding
# from backend.rag.embedder import create_embedding

# text = "The OSI model has seven layers."

# embedding = create_embedding(text)

# print("Text:")
# print(text)

# print("\nEmbedding:")
# print(embedding)

# print("\nNumber of dimensions:")
# print(len(embedding))


#====================================================================================================


#comparing the embedding of 3 sentences
# from backend.rag.embedder import create_embedding
# from sentence_transformers.util import cos_sim

# sentence_a = "The OSI model has seven layers."

# sentence_b = "How many layers are in the OSI architecture?"

# sentence_c = "Python is a programming language."

# # Create embeddings
# embedding_a = create_embedding(sentence_a)
# embedding_b = create_embedding(sentence_b)
# embedding_c = create_embedding(sentence_c)

# # Calculate cosine similarity
# similarity_ab = cos_sim(embedding_a, embedding_b)
# similarity_ac = cos_sim(embedding_a, embedding_c)

# print("Sentence A:", sentence_a)
# print("Sentence B:", sentence_b)
# print("Sentence C:", sentence_c)

# print("\nSimilarity between A and B:")
# print(similarity_ab)

# print("\nSimilarity between A and C:")
# print(similarity_ac)


#=============================================================================================================


#changing 37 chunks of the pdf into embeddings and mini retrieval system Top 1 retrieval
# from backend.services.pdf_service import extract_text_from_pdf
# from backend.rag.chunker import chunk_text
# from backend.rag.embedder import create_embedding
# from sentence_transformers.util import cos_sim

# # Step 1: Extract text from PDF
# text = extract_text_from_pdf("data/uploads/sample.pdf")

# # Step 2: Create chunks
# chunks = chunk_text(text)

# # Step 3: Create embeddings for all chunks
# chunk_embeddings = []

# for chunk in chunks:
#     embedding = create_embedding(chunk)
#     chunk_embeddings.append(embedding)

# print("Number of chunks:", len(chunks))
# print("Number of embeddings:", len(chunk_embeddings))

# # Step 4: User question
# question = "How many layers are there in the OSI model?"

# # Step 5: Create embedding for the question
# question_embedding = create_embedding(question)

# # Step 6: Compare question with every chunk
# best_score = -1
# best_chunk_index = -1

# for i, chunk_embedding in enumerate(chunk_embeddings):

#     score = cos_sim(question_embedding, chunk_embedding).item()

#     if score > best_score:
#         best_score = score
#         best_chunk_index = i

# # Step 7: Show result
# print("\nQuestion:")
# print(question)

# print("\nBest similarity score:")
# print(best_score)

# print("\nMost relevant chunk:")
# print(chunks[best_chunk_index])


#================================================================================================================================


#Top K retrieval
from backend.services.pdf_service import extract_text_from_pdf
from backend.rag.chunker import chunk_text
from backend.rag.embedder import create_embedding
from sentence_transformers.util import cos_sim

# Step 1: Extract text from PDF
text = extract_text_from_pdf("data/uploads/sample.pdf")

# Step 2: Create chunks
chunks = chunk_text(text)

# Step 3: Create embeddings for all chunks
chunk_embeddings = []

for chunk in chunks:
    embedding = create_embedding(chunk)
    chunk_embeddings.append(embedding)

print("Number of chunks:", len(chunks))
print("Number of embeddings:", len(chunk_embeddings))

# Step 4: User question
question = "How many layers are there in the OSI model?"

# Step 5: Create embedding for the question
question_embedding = create_embedding(question)

# Step 6: Compare question with every chunk
scores = []

for i, chunk_embedding in enumerate(chunk_embeddings):

    score = cos_sim(question_embedding, chunk_embedding).item()

    scores.append((score, i))

# Step 7: Sort chunks by similarity score
scores.sort(reverse=True)

# Step 8: Get Top K chunks
top_k = 3

top_results = scores[:top_k]

# Step 9: Show results
print("\nQuestion:")
print(question)

print("\nTop", top_k, "most relevant chunks:\n")

for score, index in top_results:
    print("Similarity Score:", score)
    print("Chunk:")
    print(chunks[index])
    print("-" * 50)
    print()

