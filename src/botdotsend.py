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
bot = telepot.Bot("")

# retorna ultima mensagem
print(bot.getUpdates())

# Manda uma mensagem
print(bot.sendMessage(101308303, 'bora tomar coca.'))

print(bot.getMe())

#class MandaMensagem(object):
#    """docstring para MandaMensagem."""
#    def __init__(self, arg):
#        super(MandaMensagem, self).__init__()
#        self.arg = arg
#        
#    def (self):
#        pass
