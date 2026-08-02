from vectorstore import load_vectorstore
from chatbot import ask_question

db = load_vectorstore()

question = input("Enter your question: ")

answer = ask_question(db, question)

print("\nAnswer:\n")
print(answer)