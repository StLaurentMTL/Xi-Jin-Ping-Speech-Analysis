from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from pathlib import Path
import pprint
import json

FILEPATH = Path(__file__).parent.parent / "corpus/all_tokens.json"
print(FILEPATH)

with open(FILEPATH,"r") as f:

    all_tokens = json.load(f)

chatbot = ChatBot("ChatXiPT")

trainer = ListTrainer(chatbot)
trainer.train(all_tokens)  # ONLY if this is conversational text

exit_conditions = (":q","quit","exit")

pprint.pprint("=====================哈喽！欢迎来ChatXiPT================")

while True:
    query = input("You: ")

    if query in exit_conditions:
        break 
    else:
        print(f"ChatXiPT ☭ {chatbot.get_response(query)}")