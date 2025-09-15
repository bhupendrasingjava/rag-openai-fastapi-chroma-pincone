from langchain_openai import ChatOpenAI
from langchain.chains import RetrievalQA
from app.config import OPENAI_API_KEY
from app.services.vector_service import get_vector_store

def answer_query(question: str) -> str:
    llm = ChatOpenAI(openai_api_key=OPENAI_API_KEY)
    vector_store = get_vector_store()
    rag_chain = RetrievalQA.from_chain_type(llm=llm, retriever=vector_store.as_retriever())
    return rag_chain.invoke({"query": question})["result"]
