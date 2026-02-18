from app.rag.service import ask_question

history = []

class RagService():
    def generate_response(self, query:str):
        answer = ask_question(user_query=query, history=history)

        return answer