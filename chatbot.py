faqs = {
    "what is your name": "I am a chatbot.",
    "how are you": "I am fine, thank you!",
    "what is java": "Java is a programming language.",
    "what is python": "Python is a popular programming language.",
    "who created you": "I was created as part of an AI project."
}

def get_response(user_input):
    user_input = user_input.lower()

    for question in faqs:
        if question in user_input:
            return faqs[question]

    return "Sorry, I don't understand your question."

while True:
    print("\nType 'exit' to quit")
    user = input("You: ")

    if user.lower() == "exit":
        break

    response = get_response(user)
    print("Bot:", response)