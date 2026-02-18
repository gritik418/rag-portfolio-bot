from app.rag.service import ask_question
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: str | None = None):
    return {"item_id": item_id, "q": q}


history = []

if __name__ == "__main__":
    print("Ask me questions! Type 'quit' to exit.")

    while True:
        query = input("\nYour question: ")

        if query.lower().strip() == "quit":
            print("\nGoodbye :)")
            break

        print("\nGenerating response...\n\n")
        answer = ask_question(user_query=query, history=history)
        print(answer)