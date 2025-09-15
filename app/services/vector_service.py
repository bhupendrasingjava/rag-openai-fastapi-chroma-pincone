import os
from typing import List
from langchain_core.documents import Document
from langchain_pinecone import PineconeVectorStore
from app.services.embedding_service import embedding_model
from app.config import PINECONE_API_KEY, PINECONE_ENVIRONMENT, PINECONE_INDEX_NAME

from pinecone import Pinecone, ServerlessSpec

# Initialize Pinecone client
pc = Pinecone(api_key=PINECONE_API_KEY)

def save_to_vector_store(chunks: List[Document]) -> None:
    # Create index if it doesn't exist
    index_list = pc.list_indexes().names()
    if PINECONE_INDEX_NAME not in index_list:
        pc.create_index(
            name=PINECONE_INDEX_NAME,
            dimension=1536,  # Ensure this matches your embedding model
            metric="cosine",
            spec=ServerlessSpec(
                cloud="aws",
                region="us-east-1"  # Match your Pinecone console region
            )
        )

    # Use langchain-pinecone to add documents
    PineconeVectorStore.from_documents(
        documents=chunks,
        embedding=embedding_model,
        index_name=PINECONE_INDEX_NAME
    )

def get_vector_store() -> PineconeVectorStore:
    return PineconeVectorStore.from_existing_index(
        index_name=PINECONE_INDEX_NAME,
        embedding=embedding_model
    )
