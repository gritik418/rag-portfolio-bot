from app.rag.service import ask_question
from fastapi import FastAPI
from app.routes.rag import router

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

app.include_router(router)

@app.get("/items/{item_id}")
def read_item(item_id: int, q: str | None = None):
    return {"item_id": item_id, "q": q}

