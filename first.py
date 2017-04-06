from chatterbot import ChatBot
import fileinput

print("hello chatbot")
chatbot = ChatBot(
    'Ron Obvious',
    trainer='chatterbot.trainers.ChatterBotCorpusTrainer'
)

print(" chatbot is getting trained")
# Train based on the english corpus
chatbot.train("chatterbot.corpus.english")

print(" chatbot is going to give your reply")
# Get a response to an input statement

while True:
	print("\nWrite You question and hit Enter.\n Qustion plz :")
	for line in fileinput.input():
		#print("\nyour Question is : " + str(line))
		print("\nDwijen : " + str(chatbot.get_response(str(line))))
		print("\n Question:->")
		
