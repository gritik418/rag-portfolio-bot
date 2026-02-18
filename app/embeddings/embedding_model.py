from langchain_ollama.embeddings import OllamaEmbeddings
from app.config.default import EMBEDDING_BASE_URL,EMBEDDING_MODEL

def get_embedding_model():
    model = OllamaEmbeddings(
        base_url=EMBEDDING_BASE_URL,
        model=EMBEDDING_MODEL,
    )

    return model
