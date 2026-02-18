from fastapi import APIRouter
from app.services.rag_service import RagService

router = APIRouter()
rag_service = RagService()

@router.post("/query")
def query_rag(payload):
    print(payload)
    answer = rag_service.generate_response(query=payload)

    return {"answer": answer}
