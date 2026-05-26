import streamlit as st

from app.pdf_handler import read_pdf
from app.vector_store import build_vector_store, search_document
from app.chatbot import ask_question

st.set_page_config(page_title="Ask My PDF", layout="wide")

st.title("Ask My PDF Bot")

if "ready" not in st.session_state:
    st.session_state.ready = False

if "messages" not in st.session_state:
    st.session_state.messages = []

uploaded_file = st.file_uploader("Upload PDF", type=["pdf"])

if uploaded_file and not st.session_state.ready:

    with st.spinner("Processing PDF..."):

        pdf_content = read_pdf(uploaded_file)

        index, texts, metadata = build_vector_store(pdf_content)

        st.session_state.index = index
        st.session_state.texts = texts
        st.session_state.metadata = metadata
        st.session_state.ready = True

    st.success("PDF ready")

if st.session_state.ready:

    st.subheader("Chat")

    for msg in st.session_state.messages:
        with st.chat_message(msg["role"]):
            st.markdown(msg["content"])

    question = st.chat_input("Ask from PDF")

    if question:

        st.session_state.messages.append(
            {"role": "user", "content": question}
        )

        with st.chat_message("user"):
            st.markdown(question)

        matches = search_document(
            question,
            st.session_state.index,
            st.session_state.texts,
            st.session_state.metadata
        )

        answer, pages = ask_question(question, matches)

        response = f"{answer}\n\nSources: {pages}"

        st.session_state.messages.append(
            {"role": "assistant", "content": response}
        )

        with st.chat_message("assistant"):
            st.markdown(response)

else:
    st.info("Upload a PDF to start")