#-------------------------------------------------------------------------------
# Name:        AlgunNombreADeTener
# Purpose:     Sacar Nota
#
# Author:      Alguien
#
# Created:     Hace Mucho
# Copyright:   (c) lenovo 2020
# Licence:     <Uranus>
#-------------------------------------------------------------------------------

import random

class Objeto:
    def __init__(self):
        pass

    def getString(self):
        pass

class ObjetoReal(Objeto):

    def getString(self):
        return "Imprimiendo una cadena"

class Proxy(Objeto):
    def __init__(self):
        self.__obj = ObjetoReal()

    def getString(self):
        return self.__obj.getString()

class OtroObjeto:
    def __init__(self):
        pass

    def doSomething(self):
        return "Imprimiendo una cadena"

class Adapter(Objeto):
    def __init__(self):
        self.__obj = OtroObjeto()

    def getString(self):
        return self.__obj.doSomething()

def main():
    prx = Proxy()
    ada = Adapter()
    obj = Objeto()
    if random.randint(0,3) <= 1:
        obj = prx
    else:
        obj = ada
    print(obj.getString(), "desde", type(obj))
    pass

if __name__ == '__main__':
    main()
