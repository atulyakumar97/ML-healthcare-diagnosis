from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import os

bot = ChatBot('Bot',
              storage_adapter='chatterbot.storage.SQLStorageAdapter',
              trainer='chatterbot.trainers.ListTrainer')
trainer=ListTrainer(bot)

for files in os.listdir("./data"):
      data = open("./data/"+files ,'r').readlines()
      print(files)
      trainer.train(data)
     
while True:
    
    message =input("you:")
    if message.strip()!='Bye' or message.strip()=='bye':
        reply=bot.get_response(message)
        print('Chatbot :',reply)
    
    if message.strip()=="Bye" or message.strip()=='bye':
        print ("Chatbot :Bye")
        break
    
