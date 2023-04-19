
main = {}
backup = {}

op = 1
tam = 0
while op!= 0:
    tam += 1
    print('Cadastro da pessoa')

    main[tam] = {tam: input('nome:')}
    backup[tam] = main[tam]
    if tam % 5 == 0:
        for i,pessoa in main.items():
            print(main[i])
        main.clear()
                  
    op = int(input('1->continuar\n0->encerrar '))

