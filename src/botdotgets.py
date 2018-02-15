#!~/anaconda3/bin/python
# -*- coding: utf-8 -*-

""" Neviim - 2018

    Descritivo:
        Um bot para ser utilizado no telegram

    depende:
        $ pip3 install telepot

    Uso:
        $ 
""" 

import telepot

# inicializa com o tokey o bot
bot = telepot.Bot("436561103:AAEN7Ft2u2OHzYrpNOy8hrm8OueuJgjx6K8")

def recebeMensagem(mensagem):
    print(mensagem['text'])

bot.message_loop(recebeMensagem)

while True:
    pass