from langchain_ollama import ChatOllama
from app.config.default import LLM_BASE_URL,LLM_MODEL,LLM_TEMP


def get_llm():
    model = ChatOllama(
        model=LLM_MODEL,
        base_url=LLM_BASE_URL,
        temperature=LLM_TEMP
    )

    return model