from langchain_chroma import Chroma
from app.embeddings.embedding_model import get_embedding_model
from app.config.default import CHROMA_PERSIST_DIR
from pathlib import Path
import shutil

DB_PATH = CHROMA_PERSIST_DIR

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