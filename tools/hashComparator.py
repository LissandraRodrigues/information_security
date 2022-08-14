import hashlib

file1 = 'text_1.txt'
file2 = 'text_2.txt'

hash1 = hashlib.new('ripemd160')
hash1.update(open(file1, 'rb').read())

hash2 = hashlib.new('ripemd160')
hash2.update(open(file2, 'rb').read())

if hash1.digest() != hash2.digest():
    print("Hash's diferentes!")
    print(f'O arquivo: {file1} é diferente do arquivo: {file2}.')
else:
    print("Hash's iguais!")
    print(f'O arquivo: {file1} é igual ao arquivo: {file2}.')

print(f'\nHash do arquivo: {file1} é: {hash1.hexdigest()}')
print(f'Hash do arquivo: {file2} é: {hash2.hexdigest()}')