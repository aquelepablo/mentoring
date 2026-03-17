"""
5. Aprovado ou Reprovado: Peça três notas de um aluno. Calcule a média.
● Média 7 ou mais: Aprovado
● Média entre 5 e 6.9: Recuperação
● Média abaixo de 5: Reprovado
"""

print("---| Validação de Notas |---")

first_grade = float(input("Informe a sua primeira nota: "))
second_grade = float(input("Informe a sua segunda nota: "))
third_grade = float(input("Informe a sua terceira nota: "))

average_grade = (first_grade + second_grade + third_grade)/3

if average_grade >= 7:
    print(f"Aprovado - Média: {average_grade}")
elif average_grade < 5:
    print(f"Reprovado - Média: {average_grade}")
else:
    print(f"Recuperação - Média: {average_grade}")