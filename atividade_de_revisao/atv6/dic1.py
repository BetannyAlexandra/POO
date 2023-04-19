num = int(input('informe o numero de dados que deseja inserir'))
contatos = []
for i in range(num):
    dicionario = {"cpf": input('insira seu cpf'),
                  "nome": input('insira seu nome'),
                  "idade": input('insira sua idade'),
                  "telefone": input('insira seu telefone'),
                  }
    contatos.append(dicionario)

print(contatos)
