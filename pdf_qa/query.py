# pdf_qa/query.py
import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough

from pdf_qa.config import VECTORSTORE_PATH, EMBEDDING_MODEL_NAME, GEMINI_MODEL

load_dotenv()


def get_retriever():
    embeddings = HuggingFaceEmbeddings(model_name=EMBEDDING_MODEL_NAME)
    vectorstore = FAISS.load_local(
        VECTORSTORE_PATH, embeddings, allow_dangerous_deserialization=True
    )
    return vectorstore.as_retriever()


def format_docs(docs):
    return "\n\n".join(doc.page_content for doc in docs)


def ask_question(question: str) -> str:
    retriever = get_retriever()

    llm = ChatGoogleGenerativeAI(
        model=GEMINI_MODEL,
        temperature=0,
        google_api_key=os.getenv("GOOGLE_API_KEY"),
        streaming=True,
    )

    prompt = ChatPromptTemplate.from_template(
        """Answer the question based ONLY on the following context:
{context}

Question: {question}
"""
    )

    rag_chain = (
        {"context": retriever | format_docs, "question": RunnablePassthrough()}
        | prompt
        | llm
    )

    for chunk in rag_chain.stream(question):
        yield chunk.content
