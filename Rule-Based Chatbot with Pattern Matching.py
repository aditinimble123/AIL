def chatbot(message):

    message = message.lower()

    if "hello" in message or "hi" in message:
        return "Hello! How are you?"

    elif "name" in message:
        return "I am a simple chatbot."

    elif "how are you" in message:
        return "I am fine. Thank you!"

    elif "help" in message:
        return "How can I help you?"

    elif "bye" in message:
        return "Goodbye!"

    else:
        return "Sorry, I don't understand."


print("Chatbot started!")

while True:

    user = input("You: ")

    response = chatbot(user)

    print("Bot:", response)

    if "bye" in user.lower():
        break