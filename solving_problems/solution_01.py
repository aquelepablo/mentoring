print("--- Onde você está no jogo da vida? ---\n")

name = input("Digite seu primeiro nome: ")
age = int(input("Digite a sua idade: "))

#print("\n")

if age > 65:
    print(f"Você se aposentou {name}. Hora de redescobrir a vida.")

elif age >= 18:
    print(f"{name}, você é um adulto. Pague seus boletos e curta a vida.")

else:
    print(f"Menor de idade você é, {name} padawan.")

print("")