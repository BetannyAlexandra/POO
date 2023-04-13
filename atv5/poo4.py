
cont=0
vogal=['a','e','i','o','u']
nome = (input('informe uma palavra'))

for let in nome:
    print(let)

    
    listavogal= [let for let in nome if  let not in vogal]
  


print(len(listavogal)),

print(listavogal)


