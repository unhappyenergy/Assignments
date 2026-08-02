import os
import streamlit as st
from vectorstore import create_vectorstore, load_vectorstore
from chatbot import ask_question

st.set_page_config(
    page_title="Document Question Answering",
    layout="wide"
)
st.title("Document Question Answering System")

uploaded_file = st.file_uploader(
    "Upload a PDF",
    type="pdf"
)

if uploaded_file is not None:
    pdf_path = "uploaded_document.pdf"
    with open(pdf_path, "wb") as f:
        f.write(uploaded_file.getbuffer())

    # every uploaded file will create a new vectorstore
    if os.path.exists("vector_db"):
        import shutil
        shutil.rmtree("vector_db")
        
    create_vectorstore(pdf_path)
    db = load_vectorstore()

    question = st.text_input("Ask a question")
    if question:
        with st.spinner("Generating answer :"):
            answer = ask_question(db, question)

        st.subheader("Answer")
        st.write(answer)