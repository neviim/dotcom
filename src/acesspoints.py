#!~/anaconda3/bin/python
# -*- coding: utf-8 -*-

""" Neviim - 2018

    Descritivo:
        Este codigo é de carater academigo, qualquer mal 
        uso é de responsabilidade de quem o utilizar.

    depende:
        $ sudo pip install access_points

    Uso:
        $ access_points
""" 

from access_points import get_scanner

class Scan(object):
    """ docstring para Scan."""
    def __init__(self):
        super(Scan, self).__init__()
        self.wifi_scanner = get_scanner()
        
    def roteador(self):
        """ Procura por roteadores:

            Returns:
                lista -- Contem todos os acess point encontrados

                        Retorna as seguintes informaçoes:
                        ssid       -> Nome do acesso.
                        bssid      -> Mac Adress do radio.
                        quality    -> Qualidade do Acesso.
                        security   -> Tipo de segurança utilizado.
        """
        lista = []
        for ap in self.wifi_scanner.get_access_points():
            lista.append(ap)
        return lista

# 
if __name__ == '__main__':
    """ lista todos acesspoint ao alcanse
    """
    scan = Scan()
    radios = scan.roteador()

    # radios encontrados
    for radio in radios:
        print(radio)


