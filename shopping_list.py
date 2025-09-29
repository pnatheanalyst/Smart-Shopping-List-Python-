#criar uma lista de produtos com preços
products = {
    'tomato': 50,
    'onion': 75,
    'rice': 100,
    'bread': 10,
    'milk': 50,
    'paper': 10,
    'water': 10,
}
#mostrar lista inicial de compras para o utilizador
print("Produtos na cesta inicial:")
for item, price in products.items():
    print(f"{item.title()}: {price:.2f} kwz")

# Calcula o total da compra
all_products = sum(products.values())
print(f"A cesta de produtos na sua totalidade vale {all_products:.2f} kwz.")

# Pede o orçamento ao utilizador
budget = int(input("Escreva o montante que quer gastar (kwz): "))

# Compara o total com o budget
if budget < all_products:
    debt = all_products - budget
    print(f"Lamento. Não tem fundos suficientes. Precisa de mais {debt:.2f} kwz.")
elif budget > all_products:
    change = budget - all_products
    print(f"Obrigado(a) pela compra. Aqui está o seu troco: {change:.2f} kwz.")
else:
    print("Obrigado(a) pela compra. Volte sempre.")