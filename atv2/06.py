valor=int(input(' Informe um valor'));

#total a pagar com o desconto

desconto=valor-(valor*0.10)
print('Valor com desconto',desconto)

parcelas=desconto/3

print('Valor das parcelas',parcelas)

comissao=desconto*0.05

print('Comissão do vendedor',comissao)
