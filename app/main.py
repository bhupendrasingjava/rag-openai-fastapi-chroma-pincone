from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes import ingest_routes, query_routes

app = FastAPI(
    title="RAG with OpenAI-Pinecone ..",
    description="API for Retrieval-Augmented Generation using OpenAI and LangChain",
    version="1.0.0"
)

# CORS middleware - useful if frontend apps access your API
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Change to your frontend URLs in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(ingest_routes.router, prefix="/ingest", tags=["Document Ingestion"])
app.include_router(query_routes.router, prefix="/query", tags=["Query"])

@app.get("/")
def root():
    return {"message": "Welcome to the RAG with OpenAI API. Visit /docs for documentation."}
