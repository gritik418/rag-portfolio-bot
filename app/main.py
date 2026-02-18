from app.rag.service import ask_question

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