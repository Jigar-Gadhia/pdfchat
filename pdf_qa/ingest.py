import os
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from .config import (
    PDF_SOURCE_DIR,
    VECTORSTORE_PATH,
    CHUNK_SIZE,
    CHUNK_OVERLAP,
    EMBEDDING_MODEL_NAME,
)


def ingest_pdfs():
    # Load all PDFs in source_pdfs
    docs = []
    for file in os.listdir(PDF_SOURCE_DIR):
        if file.endswith(".pdf"):
            loader = PyPDFLoader(os.path.join(PDF_SOURCE_DIR, file))
            docs.extend(loader.load())

    if not docs:
        raise ValueError("No PDFs found in data/source_pdfs/")

    # Split
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=CHUNK_SIZE, chunk_overlap=CHUNK_OVERLAP
    )
    chunks = text_splitter.split_documents(docs)

    # Embed and store
    embeddings = HuggingFaceEmbeddings(model_name=EMBEDDING_MODEL_NAME)
    vectorstore = FAISS.from_documents(chunks, embeddings)
    vectorstore.save_local(VECTORSTORE_PATH)
    print(f"✅ Ingested {len(chunks)} chunks into {VECTORSTORE_PATH}")


if __name__ == "__main__":
    ingest_pdfs()
