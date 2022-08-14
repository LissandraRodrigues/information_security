import socket

connection = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

print("\n")
print("#" * 80)

print("Socket criado com sucesso!\n")

host = 'localhost'
port = 5432

connection.bind((host, port))

message = "\nServer: Hello, Client"

while True:
    data, address = connection.recvfrom(4096)

    if data:
        print("Servidor enviando mensagem.")
        connection.sendto(data + (message.encode()), address)
