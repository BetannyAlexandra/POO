class Item:
  def __init__(self, nome: str, preco: float):
    self.__nome = nome
    self.__preco = preco


class Pedido:
  def __init__(self, numero, data):
#  self.__numero = numero
    self.__data = data
    self.__itens = []

  def adicionar_item(self, item: Item):
    self.__itens.append(item)

  def listar_itens(self):
    for item in self.__itens:
      print("Produto:", item.nome, "Data:", self.__data)

class Cliente:
  def __init__(self, nome: str, email: str):
    self.__nome = nome
    self.__email = email
    self.__listaPedidos = []

  def adicionar_pedido(self, pedido: Pedido):
    self.__listaPedidos.append(pedido)

  def listar_pedidos(self):
    for pedido in self.__listaPedidos:
      print("Número:", pedido.numero, "Data:", pedido.data)

  @property
  def nome(self):
    return self.__nome

  @property
  def email(self):
    return self.__email


# Cadastrando um cliente
cliente1 = Cliente("João", "joao@example.com")

# Criando um pedido para o cliente
pedido1 = Pedido(1, "2023-05-16")

# Adicionando produtos ao pedido
produto1 = Item("Camiseta", 29.99)
produto2 = Item("Calça", 49.99)

pedido1.adicionar_item(produto1)
pedido1.adicionar_item(produto2)

# Associando o pedido ao cliente
cliente1.adicionar_pedido(pedido1)

# Exibindo os detalhes do cliente, seus pedidos e os produtos de cada pedido
print("Detalhes do Cliente:")
print(f"Nome: {cliente1.nome}")
print(f"E-mail: {cliente1.email}")

print("\nPedidos do Cliente:")
cliente1.listar_pedidos()