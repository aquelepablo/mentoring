"""
10. Simulador de Caixa Eletrônico:
Peça ao usuário o valor que ele deseja sacar (número inteiro). 
Suponha que o caixa tem notas de € 50, € 20 e € 10. 
O programa deve dizer quantas notas de cada valor serão entregues para minimizar a quantidade de notas. 
Dica: Use a divisão inteira // e o resto da divisão % junto com os ifs para verificar quais notas podem ser usadas.
"""

print("---| Simulador de Caixa Eletrônico |---\n")

try:
    withdraw = int(input("Informe o valor que deseja sacar: "))
except ValueError:
    print("Deve ser informado um número válido")
    exit()

if (withdraw < 10 or withdraw % 10 > 0):
    print("Deve ser informado um número multiplo de 10")
    exit()

print(withdraw % 10)

value_50 = 50
value_20 = 20
value_10 = 10

bills_50 = 0
bills_20 = 0
bills_10 = 0

remaining_value = withdraw

result = f"Você realizou um saque de €{withdraw} em:"

if remaining_value // value_50 > 0:
    bills_50 = remaining_value // value_50
    remaining_value = remaining_value - (bills_50 * value_50)
    result += f"\n> Notas de €{value_50}: {bills_50}"
    
if remaining_value // value_20 > 0:
    bills_20 = remaining_value // value_20
    remaining_value = remaining_value - (bills_20 * value_20)
    result += f"\n> Notas de €{value_20}: {bills_20}"

if remaining_value // value_10 > 0:
    bills_10 = remaining_value // value_10
    remaining_value = remaining_value - (bills_10 * value_10)
    result += f"\n> Notas de €{value_10}: {bills_10}"

print(result)

