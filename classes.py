class Conta:
    def __init__(self,nome,saldo): 
        self.nome=nome
        self.saldo=saldo
conta_a= Conta('Taylor',10000)
print(conta_a.nome,conta_a.saldo)
