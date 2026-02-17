from langchain_community.document_loaders import DirectoryLoader, TextLoader
import os 

def load_text_files(text_dir_path: str):
    if not os.path.exists(text_dir_path):
        raise FileNotFoundError(f"Text files not found: {text_dir_path}")

    loader = DirectoryLoader(
        path=text_dir_path,
        glob="**/*.txt",
        loader_cls=TextLoader,
    )

    documents = loader.load()

    if not documents:
        raise ValueError("No Text files found in the directory.")
    
    return documents