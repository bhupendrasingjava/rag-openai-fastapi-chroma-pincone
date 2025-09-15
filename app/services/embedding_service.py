from langchain_openai import OpenAIEmbeddings
from app.config import OPENAI_API_KEY

embedding_model = OpenAIEmbeddings(openai_api_key=OPENAI_API_KEY)
