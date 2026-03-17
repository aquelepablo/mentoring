"""
7. Analisador de Triângulos:
Peça três medidas (A, B, C). 
Primeiro, verifique se elas podem formar um triângulo 
    (cada lado deve ser menor que a soma dos outros dois). 
Se sim, diga se o triângulo é 
    Equilátero (3 lados iguais), 
    Isósceles (2 iguais) 
    ou Escaleno (todos diferentes).
"""

print("---| Analisador de Triângulos |---")

side_a, side_b, side_c = input("Informe os 3 lados de um triangulo separados por vírgula (A, B, C): ").split(",")

side_a = int(side_a)
side_b = int(side_b)
side_c = int(side_c)

if not (side_a < (side_b + side_c) and side_b < (side_a + side_c) and side_c < (side_a + side_b)):
    print("Os lados informados não podem formar um triângulo.")
    exit()

if side_a == side_b == side_c:
    print("Esse é um triângulo equilátero")

elif side_a == side_b or side_b == side_c or side_a == side_c:
    print("Esse é um triangulo isóceles")

else:
    print("Esse é um triangulo escaleno")