import socket

connection = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

print("\n")
print("#" * 80)

print("Socket criado com sucesso!\n")

host = 'localhost'
port = 5432

message = "Hello, Server"

try:
    connection.sendto(message.encode(), (host, port))

    data, server = connection.recvfrom(4096)
    data = data.decode()

    print("Cliente: {}".format(data))

finally:
    print("\n")
    print("#" * 80)
    print("Conexão encerrada com sucesso!")
    connection.close()