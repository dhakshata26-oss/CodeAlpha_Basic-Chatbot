def basic_chatbot():
    print("Chatbot: Hello! I am a simple rule-based chatbot. Type 'bye' to exit.")
    while True:
        user_input = input("You: ").strip().lower()
        if user_input == "hello":
            print("Chatbot: Hi!")
        elif user_input == "how are you":
            print("Chatbot: I'm fine, thanks!")
        elif user_input == "bye":
            print("Chatbot: Goodbye!")
        else:
            print("Chatbot: I'm sorry, I don't understand that. You can try saying 'hello', 'how are you', or 'bye'.")
if __name__ == "__main__":
    basic_chatbot()
