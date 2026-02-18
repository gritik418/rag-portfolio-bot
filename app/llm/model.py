from langchain_ollama import ChatOllama


def get_llm():
    model = ChatOllama(
        model="phi3",
        base_url="http://localhost:12434",
        temperature=0.2
    )

    return model