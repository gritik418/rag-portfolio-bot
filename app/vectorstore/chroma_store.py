from langchain_chroma import Chroma
from app.embeddings.embedding_model import get_embedding_model
from pathlib import Path
import shutil

BASE_DIR = Path(__file__).resolve().parent.parent.parent
DB_PATH = BASE_DIR / "chroma-store"

def create_vectorstore(documents):
    if DB_PATH.exists():
        shutil.rmtree(DB_PATH)

    embedding_model = get_embedding_model()

    vector_store = Chroma.from_documents(
        documents=documents,
        embedding=embedding_model,
        persist_directory=str(DB_PATH),
        collection_metadata={"hnsw:space": "cosine"}
    )

    return vector_store


def get_vectorstore():
    if not DB_PATH.exists():
        raise ValueError("Vectorstore not found.")
    
    embedding_model = get_embedding_model()

    db = Chroma(
        persist_directory=str(DB_PATH),
        embedding_function=embedding_model
    )

    return db