from langchain_community.document_loaders import DirectoryLoader, PyMuPDFLoader
import os

def load_pdf(pdf_dir_path: str):
    if not os.path.exists(pdf_dir_path):
        raise FileNotFoundError(f"PDF directory not found: {pdf_dir_path}")
    
    loader = DirectoryLoader(
        path=pdf_dir_path,
        glob="**/*.pdf",
        loader_cls=PyMuPDFLoader,
    )

    documents = loader.load()

    if not documents:
        raise ValueError("No PDF files found in the directory.")

    return documents