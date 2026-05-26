from langchain_text_splitters import RecursiveCharacterTextSplitter
from sentence_transformers import SentenceTransformer
import faiss
import numpy as np
model = SentenceTransformer("all-MiniLM-L6-v2")
def build_vector_store(pdf_content):
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=700,
        chunk_overlap=150
    )
    texts = []
    metadata = []
    for item in pdf_content:
        chunks = splitter.split_text(item["text"])

        for chunk in chunks:
            texts.append(chunk)
            metadata.append(
                {
                    "page": item["page"]
                }
            )
    embeddings = model.encode(texts)
    dimension = embeddings.shape[1]
    index = faiss.IndexFlatL2(dimension)
    index.add(np.array(embeddings))
    return index, texts, metadata
def search_document(question, index, texts, metadata):
    question_embedding = model.encode([question])
    _, indices = index.search(
        np.array(question_embedding),
        k=4
    )
    matches = []
    for i in indices[0]:
        matches.append(
            {
                "text": texts[i],
                "page": metadata[i]["page"]
            }
        )
    return matches