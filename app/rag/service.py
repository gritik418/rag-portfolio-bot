from app.retrieval.retriever import get_retriever
from app.rag.query_rewriter import rewrite_query
from app.llm.model import get_llm
from langchain_core.messages import HumanMessage, SystemMessage, AIMessage

def ask_question(user_query: str, history: list):
    retriever = get_retriever(k=6)
    query = rewrite_query(query=user_query, history=history)

    relevant_docs = retriever.invoke(query)

    prompt = f"""
        You are a helpful assistant answering questions about Ritik.

        Use the provided context to answer clearly and professionally.

        If partial information is available, summarize what is known.
        Only say you don't have enough information if absolutely nothing relevant is found.

        Context:
        {"".join([f"\n---\n{doc.page_content}\n" for doc in relevant_docs])}

        Question:
        {user_query}

        Answer:
    """

    messages = [
        SystemMessage(content="You are a helpfull assistant"),
        HumanMessage(content=prompt)
    ]

    llm = get_llm()

    answer = llm.invoke(messages)

    history.append(HumanMessage(content=query))
    history.append(AIMessage(content=answer.content))

    return answer.content
