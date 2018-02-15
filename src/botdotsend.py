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
from pprint import pprint
import telepot

# inicializa com o tokey o bot
bot = telepot.Bot("436561103:AAEN7Ft2u2OHzYrpNOy8hrm8OueuJgjx6K8")

# retorna ultima mensagem
response = bot.getUpdates()
pprint(response)

# Manda uma mensagem
#print(bot.sendMessage(101308303, 'bora tomar coca.'))

print(bot.getMe())

#class MandaMensagem(object):
#    """docstring para MandaMensagem."""
#    def __init__(self, arg):
#        super(MandaMensagem, self).__init__()
#        self.arg = arg
#        
#    def (self):
#        pass
