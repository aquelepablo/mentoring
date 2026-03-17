def age_checker(name:str = None, age:int = None):

    try:
        print("--- Onde você está no jogo da vida? ---\n")

        if name is None:
            name = input("Digite seu nome: ")
        else:
            print(f"Nome informado: {name}")

        if age is None:
            age = input("Digite a sua idade: ")

        else:
            print(f"Idade informada: {age}")

        if not name:
            raise Exception("Nome deve ser informado")

        if not age:
            raise Exception("Idade deve ser informada")

        try:
            age = int(age)
        except ValueError:
            raise Exception("Deve ser informado um número válido para idade")

        if age < 1:
            raise Exception("Idade deve ser maior que zero")

        name = name.strip().capitalize()   

        if age < 18:
            print(f"Menor de idade você é, {name} padawan.")
        elif age >= 18 and age <= 65:
            print(f"{name}, você é adulto(a). Pague seus boletos e curta a vida.")
        else:
            print(f"Você se aposentou {name}. Hora de redescobrir a vida.")

    except Exception as e:
        print(e)