from backend.rag.rag_pipeline import answer_question


question = "How many layers are there in the OSI model?"

answer = answer_question(question)

print("Question:")
print(question)

print("\nAnswer:")
print(answer)