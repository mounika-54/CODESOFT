# CODESOFT
print("🤖 Welcome to Simple Chatbot!")
print("Type 'bye' to exit.\n")

while True:
    user = input("You: ").lower()

    if user == "hi" or user == "hello":
        print("Bot: Hello! How are you?")

    elif user == "how are you":
        print("Bot: I am fine. Thank you!")

    elif user == "what is your name":
        print("Bot: My name is SimpleBot.")

    elif user == "who created you":
        print("Bot: I was created using Python.")

    elif user == "bye":
        print("Bot: Goodbye! Have a nice day.")
        break

    else:
        print("Bot: Sorry, I don't understand.")
