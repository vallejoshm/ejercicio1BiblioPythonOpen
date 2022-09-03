import listaPaises

def main() :
    cadenaPaises = input('Ingrese una lista de países separados por una coma: ')
    lista = listaPaises.listaPaises(cadenaPaises)
    print(lista)

if __name__ == '__main__':
    main()
