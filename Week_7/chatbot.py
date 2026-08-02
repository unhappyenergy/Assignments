import os
import google.genai as genai
from dotenv import load_dotenv


load_dotenv()
client = genai.Client(api_key=os.getenv("GOOGLE_API_KEY"))

def ask_question(vectorstore, question):
    #gives top 3 relevant documents from the vectorstore based on the question
    docs = vectorstore.similarity_search(
        question,
        k=3
    )
    context = "\n\n".join(doc.page_content for doc in docs)
    prompt = f"""
    You are a document question answering assistant.

    Answer ONLY from the given context.

    If the answer is not present in the context, reply:

    "I could not find the answer in the uploaded document."

    Context:
    {context}

    Question:
    {question}

    Answer:
    """
    # for cleaner output if error occurs
    try:
        response = client.models.generate_content(
        model="models/gemini-3.5-flash",
        contents=prompt
        )
        return response.text
    
    except Exception as e:
        return f"Error: {e}"