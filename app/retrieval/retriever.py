from app.vectorstore.chroma_store import get_vectorstore

def get_retriever(k: int = 4):
    db = get_vectorstore()
    retriever = db.as_retriever(search_kwargs={"k": k})
    return retriever
