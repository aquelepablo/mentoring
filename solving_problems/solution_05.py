"""
2. Comparador de Números:
Peça dois números e diga qual deles é o maior ou se são iguais.
"""

print("---| Comparador de Números |---\n")

first_number = int(input("Informe o primeiro número: "))
second_number = int(input("Informe o segundo número: "))



if first_number > second_number:
    print(f"O número {first_number} é maior que o número {second_number}")

elif first_number == second_number:
    print(f"O número {first_number} é igual ao número {second_number}")

elif first_number < second_number:
    print(f"O número {second_number} é maior que o número {first_number}")

