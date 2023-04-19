salario=int(input("digite o salario"))
emprestimo=int(input("digite o valor da prestação do emprestimo"))

if emprestimo>(salario*0.20):
    print('emprestimo não concedido')
else:
      print('emprestimo concedido')