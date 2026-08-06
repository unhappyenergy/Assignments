# Document Question Answering System (RAG)

## Overview

This project is a Retrieval-Augmented Generation (RAG) based Document Question Answering System. Users can upload a PDF document and ask questions related to its content. The system retrieves the most relevant information from the document and generates an answer using Google's Gemini model.

## Features

- Upload PDF documents
- Automatic text chunking
- Semantic search using FAISS
- Question Answering using Gemini
- Simple Streamlit interface

## Technologies Used

- Python
- Streamlit
- LangChain
- FAISS
- Sentence Transformers
- Google Gemini API

## Project Structure

```
app.py
qa.py
vectorstore.py
requirements.txt
README.md
.env
```

## Installation

```bash
pip install -r requirements.txt
```

Create a `.env` file.

```
GOOGLE_API_KEY=YOUR_API_KEY
```

Run the application

```bash
streamlit run app.py
```

## Workflow

1. Upload PDF
2. Extract text
3. Split into chunks
4. Generate embeddings
5. Store embeddings in FAISS
6. Retrieve relevant chunks
7. Generate answer using Gemini
