from langchain_core.messages import SystemMessage, HumanMessage
from app.llm.model import get_llm

def rewrite_query(query: str, history: list):
    if not history:
        return query

    messages = [
       SystemMessage(
    content="""
You are a strict coreference resolution engine.

Your ONLY task is to rewrite the follow-up question by replacing pronouns
with the correct entity mentioned earlier in the conversation.

Rules:
- DO NOT answer the question.
- DO NOT add explanations, details, or examples.
- DO NOT hallucinate any information.
- Return exactly one rewritten question.
- If no rewrite is needed, return the original question unchanged.
- Output plain text only.

Examples:

Conversation history:
User: Who is Ritik?
AI: Ritik Gupta is a Full Stack Developer.
User: Tell me about his experience.

Rewrite Output:
Tell me about Ritik Gupta's experience

Conversation history:
User: What is Trackr?
AI: Trackr is a task management SaaS platform.
User: Does it support RBAC?

Rewrite Output:
Does Trackr support RBAC?
"""
),      *history,
        HumanMessage(content=f"Rewrite this question: {query}")
    ]

    llm = get_llm()
    result = llm.invoke(messages)

    rewritten = result.content.strip()

    print("\nRewritten query:", rewritten, "\n")

    return rewritten
