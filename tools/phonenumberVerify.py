import phonenumbers

from phonenumbers import geocoder

number = input('Digite o telefone (Ex.: +551140028922): ')

phone_number = phonenumbers.parse(number)

print(f"\nOrigem da ligação: {geocoder.description_for_number(phone_number, 'pt')}")


