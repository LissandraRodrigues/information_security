import hashlib

message = input("Digite a mensagem: ")

algorithm = int(input('''
### MENU - ESCOLHA O TIPO DE HASH ### 

1) MD5
2) SHA1
3) SHA256
4) SHA512 

Escolha o algoritmo do hash a ser utilizado: '''))

if algorithm == 1:
    result = hashlib.md5(message.encode('utf-8'))
    print(f"\nO hash MD5 da mensagem é: {result.hexdigest()}")
elif algorithm == 2:
    result = hashlib.sha1(message.encode('utf-8'))
    print(f"\nO hash SHA1 da mensagem é: {result.hexdigest()}")
elif algorithm == 3:
    result = hashlib.sha256(message.encode('utf-8'))
    print(f"\nO hash SHA256 da mensagem é: {result.hexdigest()}")
elif algorithm == 4:
    result = hashlib.sha512(message.encode('utf-8'))
    print(f"\nO hash SHA512 da mensagem é: {result.hexdigest()}")
else:
    print("\nEntrada inválida.")

