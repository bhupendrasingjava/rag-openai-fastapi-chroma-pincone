import os
from dotenv import load_dotenv

load_dotenv()  # Load variables from .env if available

# 🔑 OpenAI API Key
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# 🌲 Pinecone Settings
PINECONE_API_KEY = os.getenv("PINECONE_API_KEY")
PINECONE_ENVIRONMENT = os.getenv("PINECONE_ENVIRONMENT")  # e.g., "us-east-1-aws"
PINECONE_INDEX_NAME = os.getenv("PINECONE_INDEX_NAME")    # e.g., "sample-movies"
