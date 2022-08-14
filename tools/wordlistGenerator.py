import itertools

message = input("Mensagem a ser permutada: ")

characteres = itertools.permutations(message, len(message))

for character in characteres:
    print(''.join(character))
