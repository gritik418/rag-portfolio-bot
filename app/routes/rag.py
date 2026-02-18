from fastapi import APIRouter
from app.services.rag_service import RagService
from app.models.rag_schema import RAGQuery, RAGResponse

router = APIRouter()
rag_service = RagService()

@router.post("/query", response_model=RAGResponse)
def query_rag(payload: RAGQuery):
    answer = rag_service.generate_response(query=payload.query)

    return {"answer": answer}
