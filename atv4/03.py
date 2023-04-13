qnt=int(input('informe a quantidade de numeros que deseja inserir'))

maior=0
cont=0
for i in range(qnt):
    num=int(input('informe um numero'))
    if num>maior:
        maior=num
        cont+=1
    if num==maior:
        cont+=1

print("O maior número lido foi",maior)

