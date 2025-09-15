from fastapi import APIRouter, UploadFile, File, HTTPException
from app.services.loader_service import process_document

router = APIRouter()

@router.post("/upload", summary="Upload a document and split into chunks")
async def upload_doc(file: UploadFile = File(...)):
    """
    Accepts a document upload, processes it by splitting into chunks,
    and saves those chunks to the vector store.
    """
    try:
        chunks = await process_document(file)
        return {"status": "success", "chunks": len(chunks)}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
