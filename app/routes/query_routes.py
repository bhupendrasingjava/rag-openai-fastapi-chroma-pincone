from fastapi import APIRouter, HTTPException
from app.models.request_models import QueryRequest
from app.services.rag_service import answer_query

router = APIRouter()

@router.post("/ask", summary="Ask a question to the RAG system")
def ask_question(req: QueryRequest):
    """
    Accepts a user's question and returns an answer from the RAG pipeline.
    """
    try:
        response = answer_query(req.question)
        return {"answer": response}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
