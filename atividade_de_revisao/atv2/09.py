valor_seg=int(input('Informe um valor em segundos'))

hora=int(valor_seg/3600)

segundos=segundos % 3600

min =segundos//60

segundos%=60

print(hora,min,segundos)





 