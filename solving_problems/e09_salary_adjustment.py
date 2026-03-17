"""
6. Reajuste Salarial: Leia o salário de um funcionário:
● Até € 2.000: aumento de 15%
● De € 2.000,01 a € 5.000: aumento de 10%
● Acima de € 5.000: aumento de 5% 
Exiba o novo salário.
"""
#Wage increase

print("---| Cálculo de Reajuste Salarial |---\n")

actual_wage = float(input("Informe o salário atual do funcionário: "))

if actual_wage <= 2000:
    wage_raise = 15
elif actual_wage > 5000:
    wage_raise = 5
else:
    wage_raise = 10

wage_increase = round(actual_wage * wage_raise / 100, 2)

new_wage = actual_wage + wage_increase

print(f"Novo salário será de €{new_wage}, um aumento de €{wage_increase}.")