"""
2. Comparador de Números:
Peça dois números e diga qual deles é o maior ou se são iguais.
"""

from decimal import Decimal

try:

    print("---| Comparador de Números |---\n")

    first_number = input("Informe o primeiro número: ").strip()
    second_number = input("Informe o segundo número: ").strip()

    if not first_number or not second_number:
        print("Erro: É preciso informar 2 números")

    else:

        if "." in first_number and "," in first_number:
            first_number = first_number.replace(".", "")

        if "." in first_number and "," in second_number:
            second_number = second_number.replace(".", "")

        first_number = first_number.replace(",", ".")
        second_number = second_number.replace(",", ".")

        first_number = Decimal(first_number)
        second_number = Decimal(second_number)

        if first_number > second_number:
            print(f"O número {first_number} é maior que o número {second_number}")

        elif first_number == second_number:
            print(f"O número {first_number} é igual ao número {second_number}")

        else:
            print(f"O número {second_number} é maior que o número {first_number}")

except Exception:
    print("Erro: Deve informar 2 números válidos")
