import os

print("\n")
print("#" * 60)

ip_or_host = input("Digite o IP ou host a ser verificado: ")

os.system('ping -n 6 {}'.format(ip_or_host))

print("#" * 60)
