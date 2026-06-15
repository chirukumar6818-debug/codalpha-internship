# Simple Rule-Based Chatbot

print("ChatBot: Hello! Type 'bye' to exit the chat.")

while True:
    user_input = input("You: ").lower()

    if user_input == "hello" or user_input == "hi":
        print("ChatBot: Hi! How can I help you?")

    elif user_input == "how are you":
        print("ChatBot: I'm doing well. Thanks for asking!")

    elif user_input == "what is your name":
        print("ChatBot: I am a simple rule-based chatbot.")

    elif user_input == "bye":
        print("ChatBot: Goodbye! Have a great day!")
        break

    else:
        print("ChatBot: Sorry, I don't understand that.")