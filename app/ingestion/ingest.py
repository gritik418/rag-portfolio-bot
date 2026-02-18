from app.loaders.text_loader import load_text_files
from app.ingestion.splitter import split_documents
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent.parent
DOCS_PATH = BASE_DIR / "docs"

def ingest_documents(docs_path: Path):
    if not docs_path.exists():
        raise FileNotFoundError("Docs path not found.")
    
    documents = load_text_files(docs_path)

    if not documents:
        raise FileNotFoundError("No docs found.")
    
    chunks = split_documents(documents=documents, chunk_size=450)

    for i, chunk in enumerate(chunks):
        print(f"{"-" * 10} Chunk: {i} {"-" * 10}")
        print(f"{chunk.page_content}")
        print("\n")


if __name__ == "__main__":
    ingest_documents(DOCS_PATH)
