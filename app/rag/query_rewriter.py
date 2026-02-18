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
- DO NOT add explanations or extra context.
- DO NOT include any details about projects, skills, or technologies.
- DO NOT hallucinate information.
- Return exactly one rewritten question.
- If no rewrite is needed, return the original question unchanged.
- Output plain text only.

Examples:

Conversation history:
User: Who is Ritik?
AI: Ritik Gupta is a Full Stack Developer.
User: Tell me about his projects.

Rewrite Output:
Tell me about Ritik Gupta's projects

Conversation history:
User: What is Trackr?
AI: Trackr is a task management SaaS platform.
User: Does it support RBAC?

Rewrite Output:
Does Trackr support RBAC?

Conversation history:
User: What is Huddle?
AI: Huddle is a social media SaaS platform.
User: Tell me more about it.

Rewrite Output:
Tell me more about Huddle.
"""
)
,
        *history,
        HumanMessage(content=f"Rewrite this question: {query}")
    ]

    llm = get_llm()
    result = llm.invoke(messages)

    rewritten = result.content.strip()

    print("\nRewritten query:", rewritten, "\n")

    return rewritten
