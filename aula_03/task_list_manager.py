"""
Exercício 1: Gerenciador de lista de tarefas
"""

tasks = ["estudar python", "limpar quarto", "fazer exercícios"]
qty_tasks = len(tasks)

new_task = input("Informe uma tarefa: ").strip().lower()

if len(new_task.split(" ")) < 2:
    print("Erro: A tarefa deve ter ao menos duas palavras")

elif new_task in tasks:
    print("Erro: Essa tarefa já existe")

else:
    tasks.append(new_task)
    print(f"A tarefa {new_task.title()} foi incluída com sucesso.")
    print("Lista atual:")
    for item in tasks:
        print(f" - {item.title()}")

