"""
1. Verificador de Paridade
Peça ao usuário um número inteiro qualquer. O programa deve exibir se o número é "Par" ou "Ímpar".
Dica: Lembre-se do operador de resto da divisão (%). Se o resto da divisão por 2 for zero, o número é par.
"""

print("---| Verificador de Paridade |---\n")

user_number = int(input("Informe um número inteiro: "))

parity = "impar"

if (user_number%2 == 0):
    parity = "par"

print(f"O número {user_number} é {parity}")