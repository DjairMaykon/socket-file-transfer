from client import *

while True:
    option = input('1) Modo depósito\n2) Modo recuperação\n0) Encerrar\n')

    if option == '1':
        print('Iniciando modo depósito\n')

        filename = input('Informe o nome do arquivo: ')
        tolerancia = input('Informe o nível de tolerância a falhas: ')

        depositFile(filename, tolerancia)

    elif option == '2':
        print('Iniciando modo recuperação\n')
    elif option == '0':
        print('Encerrando aplicação\n')