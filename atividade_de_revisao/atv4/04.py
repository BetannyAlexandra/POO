numero= int(input('informe um numero entre 100 e 999'))


while numero < 100 or numero > 999:
  numero=int(input('Número inválido\n Informe um número entre 100 e 999: '))

print(numero//100)
num=numero%100

print(num//10)
num2=num%10 
print(num2)



