"""
3. Login e Acesso
Simule um sistema de login simples. Peça ao usuário um nome de usuário e uma senha.
● Se o usuário for "admin" e a senha for "1234", exiba: "Acesso concedido: Bem-vindo, Administrador!"
● Se o usuário for "admin" mas a senha estiver errada, exiba: "Senha incorreta!"
● Para qualquer outro usuário, exiba: "Usuário não reconhecido. Acesso negado."
"""

print("---| Login |---\n")

admin_user = "admin"
admin_pass = "1234"

user = input("Informe seu usuário: ")
senha = input("Informe sua senha: ")

print("Verificando...")

message = "Usuário não reconhecido. Acesso negado."

if user == admin_user: 
    if senha == admin_pass:
        message = "Acesso concedido: Bem-vindo, Administrador!"
    else:
        message = "Senha incorreta!"

print(message)