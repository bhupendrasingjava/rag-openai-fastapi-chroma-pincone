import os
from fastapi import UploadFile
from typing import List
from langchain_community.document_loaders import PyPDFLoader, TextLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from app.services.vector_service import save_to_vector_store
from langchain_core.documents import Document  # New recommended import

async def process_document(file: UploadFile) -> List[Document]:
    os.makedirs("docs", exist_ok=True)
    file_path = os.path.join("docs", file.filename)

    with open(file_path, "wb") as f:
        f.write(await file.read())

    # Use appropriate loader based on file type
    if file.filename.lower().endswith(".pdf"):
        loader = PyPDFLoader(file_path)
    else:
        loader = TextLoader(file_path)

    docs = loader.load()

    splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
    chunks = splitter.split_documents(docs)

    save_to_vector_store(chunks)

    return chunks
