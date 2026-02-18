from langchain_ollama.embeddings import OllamaEmbeddings

def get_embedding_model():
    model = OllamaEmbeddings(
        base_url="http://localhost:12434", # Local embedding model
        model="nomic-embed-text",
    )

    return model
