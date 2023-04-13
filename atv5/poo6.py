media=[]

for i in range(0,10):

        nota1=int(input('informe nota 1 '))
        nota2=int(input('informe nota 2 '))
        nota3=int(input('informe nota 3 '))
        nota4=int(input('informe nota 4 '))

        print('\n')
        notas=(nota1+nota2+nota3+nota4)/4
        media.append(notas)
        print(media)

for i in media:
        if i >=7:
                print('notas maior que 7=',i)





