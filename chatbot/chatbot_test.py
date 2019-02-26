# -*- coding: utf-8 -*-
"""
Created on Tue Feb 26 22:45:21 2019

@author: Atulya
"""

from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import os


bot = ChatBot('Bot',
                  storage_adapter='chatterbot.storage.SQLStorageAdapter',
    logic_adapters=[
        {
            'import_path': 'chatterbot.logic.BestMatch',
           #  'maximum_similarity_threshold' : 0.10,
           #'import_path': 'chatterbot.logic.LowConfidenceAdapter',
            # 'default_response': 'I am sorry, but I do not understand.'
        }
    ],
    trainer='chatterbot.trainers.ListTrainer')

trainer=ListTrainer(bot)

while True:
    
    message =input("you:")
    if message.strip()!='Bye' or message.strip()!='bye':
        reply=bot.get_response(message)
        print('Chatbot :',reply)
    
    if message.strip()=="Bye" or message.strip()=='bye':
        print ("Chatbot :Bye")
        break
    