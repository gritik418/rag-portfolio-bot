from pydantic import BaseModel

class RAGQuery(BaseModel):
    query: str

class RAGResponse(BaseModel):
    answer: str