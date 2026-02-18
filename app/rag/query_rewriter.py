from langchain_core.messages import SystemMessage, HumanMessage
from app.llm.model import get_llm

def rewrite_query(query: str, history: list):
    if not history:
        return query
      

    messages = [
        SystemMessage(
            content="""
            You are a coreference resolution engine.
            Your task:
                Replace pronouns in the follow-up question with the correct entity mentioned earlier.
                Rules:
                - Only use entities explicitly mentioned in the conversation.
                - Do NOT use external knowledge.
                - Do NOT guess product features.
                - Do NOT change the question meaning.
                - If no replacement is needed, return the original question unchanged.
                - Output exactly one question.
            """
        ),
        *history,
        HumanMessage(content=f"Follow-up question: {query}")
    ]  

    llm = get_llm() 

    result = llm.invoke(messages)

    return result.content.strip()