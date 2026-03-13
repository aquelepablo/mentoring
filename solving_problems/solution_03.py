#INPUTS

print("---| Triagem de Tickets |---\n")

client_type_premium = "Premium"
client_type_standart = "Standart"
client_type_educational = "Educacional"
ticket_type_error = "Erro Grave"
ticket_type_doubt = "Dúvida"
ticket_type_suggestion = "Sugestão"


client_id = int(input("Informe seu Id de Cliente: "))
client_type = input("Informe qual o seu Tipo de Cliente (Premium, Standart ou Educacional): ")
ticket_type = input("Informe o tipo da ocorrência (Erro Grave, Dúvida ou Sugestão): ")
ticket_open_time = float(input("Informe há quanto tempo o ticket está em aberto: "))

#Validations
if client_type not in (client_type_premium, client_type_standart, client_type_educational):
    print("Tipo de cliente inválido.")
    exit()

if ticket_type not in (ticket_type_error, ticket_type_doubt, ticket_type_suggestion):
    print("Tipo de ocorrência inválida.")
    exit()

if ticket_open_time < 0:
    print("Horas em aberto não podem ser negativas.")
    exit()

# Business Rules
#Critical
if (
    (client_type == client_type_premium and ticket_type == ticket_type_error) 
    or (client_type == client_type_standart and ticket_type == ticket_type_error and ticket_open_time > 24)
    ):
    ticket_priority = "Crítica"
    ticket_sla = 2
#High
elif(
    (client_type == client_type_premium and ticket_type == ticket_type_doubt)
    or (client_type == client_type_standart and ticket_type == ticket_type_error and ticket_open_time <= 24)
    or (client_type == client_type_educational and ticket_type == ticket_type_error)
    ):
    ticket_priority = "Alta"
    ticket_sla = 4

#Medium
elif(
    (client_type == client_type_premium and ticket_type == ticket_type_suggestion)
    or (client_type == client_type_standart and ticket_type == ticket_type_doubt)    
    or (client_type == client_type_educational and ticket_type == ticket_type_doubt)
):
    ticket_priority = "Média"
    ticket_sla = 8
#Low
else:
    ticket_priority = "Baixa"
    ticket_sla = 24

#Report
print("--- Relatório de Triagem de Ticket ---")
print(f" Cliente ID: {client_id}")
print(f" Tipo: {client_type}")
print(f" Estado: {ticket_type} - Aberto há {ticket_open_time}h ")
print(f"\n>>> Classificação Final <<<")
print(f" Prioridade Atribuida: {ticket_priority}")
print(f" Prazo de Resposta Estimado (SLA): {ticket_sla} horas\n")


