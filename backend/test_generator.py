# from backend.rag.generator import generate_answer


# question = "what is the first layer in the OSI model?"

# context = """
# The OSI model consists of seven layers:
# Application, Presentation, Session, Transport,
# Network, Data Link, and Physical.
# """

# answer = generate_answer(question, context)

# print("Answer:")
# print(answer)

# from backend.rag.generator import generate_answer


# question = "What is the first layer in the OSI model?"

# context = """
# The OSI model consists of seven layers:
# Application, Presentation, Session, Transport,
# Network, Data Link, and Physical.
# """

# print("QUESTION:")
# print(question)

# print("\nCONTEXT:")
# print(context)

# answer = generate_answer(question, context)

# print("\nANSWER:")
# print(answer)

from backend.rag.generator import generate_answer


question = "What is the first layer in the OSI model?"

context = """
The OSI model consists of seven layers:
Application, Presentation, Session, Transport,
Network, Data Link, and Physical.
"""

print("QUESTION:")
print(question)

print("\nCONTEXT:")
print(context)

answer = generate_answer(question, context)

print("\nANSWER:")
print(answer)