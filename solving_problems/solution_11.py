"""
8. Calculadora Simples:
Peça dois números e qual operação o usuário deseja realizar (+, -, *, /). Use if/elif para fazer o cálculo correto e trate o erro de divisão por zero.
"""

print("---| Calculadora |---\n")

math_add = "+"
math_sub = "-"
math_mult = "*"
math_div = "/"


first_number = float(input("Informe o primeiro número: "))
second_number = float(input("Informe o segundo número: "))
math_op = input("Informe a operação (+, -, *, /): ")

if math_op not in (math_add, math_sub, math_mult, math_div):
    print(f"Operação inválida: {math_op}")
    exit()

if math_op == math_add:
    result = first_number + second_number

elif math_op == math_sub:
    result = first_number - second_number

elif math_op == math_mult:
    result = first_number * second_number

else:
    if second_number == 0:
        print("Não é possível dividir por zero")
        exit()
    else:
        result = first_number / second_number
    
print(f"{first_number} {math_op} {second_number} = {result}")