"""
INPUTS:
client name
qty products bought
product value
is client vip
"""

def discount_calc(name: str, 
                  qty_products: int, 
                  product_value: float, 
                  client_vip: str,
                  ask_for_input: bool = False):

    try:

        print("--- Calculadora de Descontos --- \n")

        if ask_for_input:
            name = None
            qty_products = None
            product_value = None
            client_vip = None

            name = input("Informe o seu nome: ").strip()
            qty_products = input("Informe a quantidade de produtos comprados: ").strip()
            product_value = input("Informe o valor do produto: ").strip()
            client_vip = input("Informe se você é um cliente VIP (Sim ou Não): ").strip()

        else:
            print(f"Nome informado: {name}")
            print(f"Quantidade informada: {qty_products}")
            print(f"Valor informado do produto: {product_value}")
            print(f"Cliente é VIP: {client_vip}")
        
        if not name:
            raise Exception("Nome deve ser informado")

        if not qty_products:
            raise Exception("Quantidade deve ser informada")

        if not product_value:
            raise Exception("Valor do produto deve ser informadO")

        if not client_vip:
            raise Exception("Deve informar se o cliente é VIP: Sim ou Não")

        try:
            qty_products = int(qty_products)
        except ValueError:
            raise Exception("Quantidade deve ser um número válido")

        if qty_products < 1:
            raise Exception("Quantidade deve ser maior que zero")

        try:
            product_value = float(product_value)
        except ValueError:
            raise Exception("Quantidade deve ser um número válido")

        if product_value <= 0:
            raise Exception("Valor do produto deve ser maior que zero")

        if client_vip.lower() not in ("sim", "não", "nao"):
            raise Exception("Deve informar Sim ou Não para Cliente VIP")
        else:
            if client_vip.lower() == "sim":
                is_client_vip = True
            else:
                is_client_vip = False

        name = name.strip().capitalize()

        #Define total value
        cart_value = qty_products * product_value

        #Discount rule
        if is_client_vip:
            discount = 20
        else:
            if cart_value >= 500.00:
                discount = 10
            elif cart_value >= 200.00 and cart_value < 500.00:
                discount = 5
            else:
                discount = 0

        #Final price
        discount_value = cart_value * (discount / 100)
        cart_value_discounted = cart_value - discount_value

        #Resultado
        print(f"\nResumo da compra do cliente: {name} {'(VIP)' if is_client_vip else ''}")
        print(f"Valor Bruto: ${round(cart_value,2)}")
        print(f"Desconto Aplicado de {discount}%: ${round(discount_value, 2)}")
        print(f"Valor Final a Pagar: ${round(cart_value_discounted, 2)}\n")

    except Exception as e:
        print(f"Erro: {e}")

