"""
9. Conversor de Unidades:
Crie um programa onde o usuário digita uma distância em metros 
e escolhe se quer converter para 
    (1) Centímetros, 
    (2) Quilômetros 
    ou (3) Milímetros. 
Use as condicionais para exibir o resultado.
"""

print("---| Conversor de Unidades |---\n")




distance = float(input("Informe uma distância em metros: "))
convert_to = int(input("Escolha a medida de conversão (1 - Cm | 2 - Km | 3 - Mm): "))

if distance < 1:
    print("Informe uma distância maior ou igual a 1")
    exit()

if convert_to not in (1, 2, 3):
    print("Informe 1, 2 ou 3 para medida de conversão")
    exit()

result = f"{distance} m convertido em "

if convert_to == 1: #Centímetros
    result += f"centímetros é igual a {distance * 100} cm."
    
elif convert_to == 2: #Quilômetros
    result += f"quilômetros é igual a {distance / 1000} Km."

else: #Milímetros
    result += f"milímetros é igual a {distance * 1000} mm."
    
print(result)