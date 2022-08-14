import random, string

length = int(input("Digite o tamanho da senha que você deseja: "))

chars = string.ascii_letters + string.digits + 'çÇ!@#$%*&()=-+.,?/|'

randomCharacters = random.SystemRandom()

print(''.join(randomCharacters.choice(chars) for i in range(length)))

