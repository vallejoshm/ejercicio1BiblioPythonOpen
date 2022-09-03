from pickle import *

def listaPaises(cadena):
    cad = cadena.replace(' ', '')
    print(cad)
    lista = cad.split(',')

    for elem in lista:
        elem = elem.lstrip(' ')

    lista = set(lista)
    return lista