#INPUTS

def ticket_triage(
        client_id,
        client_type,
        ticket_type,
        ticket_open_time,       
        ask_for_input: bool = False
):

    try:

        print("---| Triagem de Tickets |---\n")

        client_type_premium = "premium"
        client_type_standard = "standard"
        client_type_educational = "educacional"
        ticket_type_error = "erro grave"
        ticket_type_doubt = "dúvida"
        ticket_type_suggestion = "sugestão"

        if ask_for_input:
            client_id = None
            client_type = None
            ticket_type = None
            ticket_open_time = None      
            
            client_id = input("Informe seu Id de Cliente: ")
            client_type = input("Informe qual o seu Tipo de Cliente (Premium, Standard ou Educacional): ")
            ticket_type = input("Informe o tipo de ticket (Erro Grave, Dúvida ou Sugestão): ")
            ticket_open_time = input("Informe há quantas horas o ticket está em aberto: ")

        else:
            print(f"Cliente ID: {client_id}")
            print(f"Tipo do Cliente: {client_type}")
            print(f"Tipo de Ticket: {ticket_type}")
            print(f"Ticket aberta a: {ticket_open_time} horas")

        if not client_id:
            raise Exception("Aviso: ID do Cliente deve ser informado.")
        
        if not client_type:
            raise Exception("Aviso: Tipo do Cliente deve ser informado.")
        
        if not ticket_type:
            raise Exception("Aviso: Tipo do Ticket deve ser informado.")
        
        if not ticket_open_time:
            raise Exception("Aviso: Quantidade de horas em aberto do Ticket deve ser informada.")

        client_id = client_id.strip().replace(" ", "").upper()
        client_type = client_type.strip().replace(" ", "").lower()
        ticket_type = ticket_type.strip().lower().replace("du", "dú").replace("tao", "tão")
        ticket_open_time = ticket_open_time.strip().replace(" ", "").replace(",", ".")

        #Validations

        if client_type not in (client_type_premium, client_type_standard, client_type_educational):
            raise Exception("Erro: Tipo de cliente inválido.")

        if ticket_type not in (ticket_type_error, ticket_type_doubt, ticket_type_suggestion):
            raise Exception("Erro: Tipo de ocorrência inválida.")

        try:

            ticket_open_time = float(ticket_open_time)

        except ValueError:
                raise Exception("Erro: Quantidade de Horas deve ser um número válido.")

        if not ticket_open_time > 0:
            raise Exception("Aviso: Quantidade de Horas em aberto deve ser maior que zero.")

        # Business Rules
        #Critical
        if (
            (client_type == client_type_premium and ticket_type == ticket_type_error) 
            or (client_type == client_type_standard and ticket_type == ticket_type_error and ticket_open_time > 24)
            ):
            ticket_priority = "Crítica"
            ticket_sla = 2
        #High
        elif(
            (client_type == client_type_premium and ticket_type == ticket_type_doubt)
            or (client_type == client_type_standard and ticket_type == ticket_type_error and ticket_open_time <= 24)
            or (client_type == client_type_educational and ticket_type == ticket_type_error)
            ):
            ticket_priority = "Alta"
            ticket_sla = 4
        #Medium
        elif(
            (client_type == client_type_premium and ticket_type == ticket_type_suggestion)
            or (client_type == client_type_standard and ticket_type == ticket_type_doubt)    
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
        print(f" Tipo: {client_type.capitalize()}")
        print(f" Estado: {ticket_type.title()} - Aberto há {ticket_open_time}h ")
        print(f"\n>>> Classificação Final <<<")
        print(f" Prioridade Atribuida: {ticket_priority}")
        print(f" Prazo de Resposta Estimado (SLA): {ticket_sla} horas\n")

    except Exception as e:
        print(e)