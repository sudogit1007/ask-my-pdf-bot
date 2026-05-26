# Ask My PDF Bot
This is a simple AI-powered chatbot that lets you upload a PDF and ask questions based on its content. It reads the document, understands the text, and gives answers using AI.

## What it does
- Upload any PDF file
- Ask questions in natural language
- Get answers based only on the document
- Shows relevant page references
- Simple web interface using Streamlit

## How it works
The PDF is split into chunks of text, converted into embeddings, and stored in a vector database. When you ask a question, it searches for the most relevant parts and sends them to a language model to generate an answer.

## Tech used
- Python  
- Streamlit  
- FAISS (vector search)  
- Google Gemini API  
- LangChain  
- Sentence Transformers  

## How to run it
Install dependencies:
```bash
pip install -r requirements.txt
