"""
INPUTS:
client name
qty products bought
product value
is client vip
"""

print("--- Calculadora de Descontos --- \n")

name = input("Informe o seu nome: ")
qty_products = int(input("Informe a quantidade de produtos comprados: "))
product_value = float(input("Informe o valor do produto: "))
is_client_vip_input = bool(input("Informe se você é um cliente VIP (Sim ou Não): ") == "Sim")

#Define total value
cart_value = qty_products * product_value

#Discount rule
if is_client_vip_input:
    discount = 20
else:
    if cart_value >= 500.00:
        discount = 10
    elif cart_value >= 200.00 and cart_value <= 499.99:
        discount = 5
    else:
        discount = 0

#Final price
discount_value = cart_value * (discount / 100)
cart_value_discounted = cart_value - discount_value

#Resultado
print(f"\nResumo da compra do cliente: {name}")
print(f"Valor Bruto: ${round(cart_value,2)}")
print(f"Desconto Aplicado: ${round(discount_value, 2)}")
print(f"Valor Final a Pagar: ${round(cart_value_discounted, 2)}\n")