"""
1. Verificador de Paridade
Peça ao usuário um número inteiro qualquer. O programa deve exibir se o número é "Par" ou "Ímpar".
Dica: Lembre-se do operador de resto da divisão (%). Se o resto da divisão por 2 for zero, o número é par.
"""
try:

    print("---| Verificador de Paridade |---\n")

    user_number = input("Informe um número inteiro: ").strip().replace(",",".")

    user_number = float(user_number)
    
    if not user_number.is_integer():
        raise Exception("Erro: Deve ser informado um número inteiro para a classificação de pa ou ímpar")

    user_number = int(user_number)

    print(f"O número {user_number} é {'par' if int(user_number) % 2 == 0 else 'ímpar'}")

except Exception as e:
    print("Erro: Deve ser informado um número válido")