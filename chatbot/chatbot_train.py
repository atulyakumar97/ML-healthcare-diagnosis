from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import os

bot = ChatBot('Bot',
              storage_adapter='chatterbot.storage.SQLStorageAdapter',
              trainer='chatterbot.trainers.ListTrainer')
trainer=ListTrainer(bot)

for files in os.listdir("./data"):
    data = open("./data/"+files ,'r', encoding="utf8").readlines()
    print(files)
    trainer.train(data)
