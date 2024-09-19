# test_chatbot.py
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

# Create a new ChatBot instance
chatbot = ChatBot('TestBot')

# Train the chatbot using the English language corpus
trainer = ChatterBotCorpusTrainer(chatbot)
trainer.train('chatterbot.corpus.english')

# Get a response from the chatbot
response = chatbot.get_response('Hello, how can I help you?')
print(response)
