from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

# Create a new chatbot instance
chatbot = ChatBot('NethBot')

# Create a new instance of the ChatterBotCorpusTrainer
trainer = ChatterBotCorpusTrainer(chatbot)

# Train the chatbot on the English language corpus
trainer.train('chatterbot.corpus.english')

def get_response(user_input):
    """Generate a response from the chatbot based on user input."""
    response = chatbot.get_response(user_input)
    return response

# Main interaction loop for the chatbot
if __name__ == "__main__":
    print("Hello! I am NethBot. How can I help you today?")
    while True:
        try:
            user_input = input("You: ")
            if user_input.lower() in ['exit', 'quit', 'bye']:
                print("NethBot: Goodbye!")
                break
            response = get_response(user_input)
            print(f"NethBot: {response}")
        except (KeyboardInterrupt, EOFError, SystemExit):
            print("\nNethBot: Goodbye!")
            break
