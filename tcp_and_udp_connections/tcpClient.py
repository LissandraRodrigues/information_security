import socket

import sys

def main():
    print("\n")
    print("#" * 80)
    try:
        connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
    except socket.error as error:
        print("\nA conexão falhou.")
        print("Erro: {}".format(error))
        sys.exit()

    print("Socket criado com sucesso!\n")

    print("#" * 80)

    hostTarget = input("Digite o host ou IP a ser conectado: ")
    portTarget = int(input("Digite a porta a ser conectada: "))

    print("\n")
    print("#" * 80)

    try:
        connection.connect((hostTarget, portTarget))
        print("Cliente TCP conectado com sucesso no Host: {} e na Porta: {}.".format(hostTarget, portTarget))
        connection.shutdown(2)
    except socket.error as error:
        print("Não foi possível conectar no Host: {} e na Porta: {}.".format(hostTarget, portTarget))
        print("Erro: {}".format(error))
        sys.exit()


if __name__ == "__main__":
    main()