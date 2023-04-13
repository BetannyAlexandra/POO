

num1=int(input("digite um numero"))
num2=int(input("digite um numero"))

if num1>num2:
    print('num1 maior')
    dif=num1-num2
    print('diferença entre eles=',dif)

elif num2>num1:
     print('num2 maior')
     dif=num2-num1
     print('diferença entre eles=',dif)

else:
     print('numeros iguais')