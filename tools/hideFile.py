import ctypes

attribute = 0x02

file = input("Digite o nome (com a extensão) do arquivo que você deseja ocultar: ")

answer = ctypes.windll.kernel32.SetFileAttributesW(f'{file}', attribute)

if answer:
    print("\nArquivo ocultado.")
else:
    print("\nArquivo não foi ocultado.")

