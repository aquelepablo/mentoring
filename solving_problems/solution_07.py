"""
4. Calculadora de IMC:
Peça o peso e a altura. Calcule o IMC (peso / altura²) e diga se está "Abaixo do peso" (<18.5), "Peso ideal" (18.5 a 24.9) ou "Sobrepeso" (25 ou mais).
"""

print("---| Calculadora de IMC |---")

below_weight = 18.5
above_weight = 25

name = input("Informe seu nome: ")
weight = float(input("Informe seu peso: "))
height = float(input("Informe sua altura: "))

imc = round(weight / height ** 2, 1)

message = f"{name}, seu IMC é {imc} e você está "

if imc < below_weight:
    message += "abaixo do peso ideal."
elif imc > above_weight:
    message += "acima do peso ideal."
else:
    message += "no peso ideal."

print(message)