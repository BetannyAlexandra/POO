listaPessoas={}

num = int(input('Insira a quantidade de pessoas que deseja cadastrar: '))

for i in range(num):
    print("\n")
    nome = input('Nome: ')
    idade = int(input('Idade: '))
    cpf = input('CPF: ')
    print("\n")
    listaPessoas[nome]={"nome":nome,
                       "idade":idade,
                       "cpf":cpf}
    
menor18={}
remove=[]

for nome,dadosPessoa in listaPessoas.items():
    if dadosPessoa["idade"]<18:
        menor18[nome]=dadosPessoa
        remove.append(nome)


for i in remove:
    del listaPessoas[i]

print(f'Pessoas maiores de 18 anos')
print(listaPessoas)