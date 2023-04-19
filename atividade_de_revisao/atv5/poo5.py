list=[]
for i in range(0,10):

    num=int(input('informe 10 valores'))
    list.append(num)

impar= [num for num in list if num%2]

print(impar)
  
  
par= [num for num in list if not num%2]


print(par)


print(list)
