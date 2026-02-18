from app.loaders.text_loader import load_text_files
from app.ingestion.splitter import split_documents
from app.vectorstore.chroma_store import create_vectorstore
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent.parent
DOCS_PATH = BASE_DIR / "docs"

def ingest_documents(docs_path: Path):
    print("🚀 Starting ingestion pipeline...")

    if not docs_path.exists():
        raise FileNotFoundError("Docs path not found.")
    
    documents = load_text_files(docs_path)

    if not documents:
        raise FileNotFoundError("No docs found.")
    
    chunks = split_documents(
        documents=documents, 
        chunk_size=750,
        chunk_overlap=150,
    )

    create_vectorstore(documents=chunks)
    print("✅ Ingestion complete. Vectorstore created.")

if __name__ == "__main__":
    ingest_documents(DOCS_PATH)
