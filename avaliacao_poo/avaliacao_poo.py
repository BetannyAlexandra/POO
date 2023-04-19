

cont_mot=0
cont_veiculos=0


veiculos={"BCC009":{"marca":"Fiat", "modelo":"UNO", "ano":"2003", 
                    "placa":"BCC009", "chassi":"36563652", "cor":"Branco","km":500},
         "BCC006":{"marca":"Fiat", "modelo":"Toro", "ano":"2003", 
                   "placa":"BCC006", "chassi":"36563652","cor":"Branco","km":500},
         "BCC008":{"marca":"Fiat", "modelo":"Argo", "ano":"2003", 
                   "placa":"BCC007", "chassi":"36563652","cor":"Branco","km":500}  }

motoristas={"11111":{"nome":"François", "CPF":"11111", "RG":"223212", "CNH":"34221"},
            "22222":{"nome":"Ana", "CPF":"22222", "RG":"223212", "CNH":"34221"},
            "33333":{"nome":"MAria", "CPF":"33333", "RG":"223212", "CNH":"34221"}}

viagens={1:{"destino":"Bacabal", 
                "origem":"Caxias", 
                "distância":200.0, 
                "motorista":motoristas["11111"], 
                "veiculo":veiculos["BCC009"]},
         2:{"destino":"Bacabal", 
                "origem":"Caxias", 
                "distância":200.0, 
                "motorista":motoristas["11111"], 
                "veiculo":veiculos["BCC009"]
               }}

manutencoes ={1:{"veiculo":veiculos["BCC009"],"data":"02-02-2023", "tipo":"preventiva","custo":1000.0},
              2:{"veiculo":veiculos["BCC009"],"data":"02-02-2023", "tipo":"preventiva","custo":1000.0} }

abastecimentos={1:{"veiculo":veiculos["BCC009"],"valor":400.0,"data":"4-2-2023","quantidade":150},
               2:{"veiculo":veiculos["BCC009"],"valor":400.0,"data":"4-2-2023","quantidade":150},
               3:{"veiculo":veiculos["BCC009"],"valor":400.0,"data":"4-2-2023","quantidade":150},}




def menu():

   
    global dados,cod_manutencao,cod_abastec,cont_mot,cont_veiculos
    dados=1
    cod_manutencao=3
    cod_abastec=4

        
    opcao = 15
    while opcao != 0:
        opcao = int(input("-----------MENU-----------\n"
"1-Gerenciamento de Motoristas\n"
"2-Gerenciamento de Veículos\n"
"4-Gerenciamento de  Viagem\n"
"5-Registrar Abastecimento\n"
"6-Registrar Manutenção\n"
"7-Relatório\n"))
        

        if opcao == 1:
            op=input("a-Cadastrar Novo Motorista\n"
    "b-Pesquisar Motorista\n"
    "c-Editar Motorista\n"
    "d-Deletar Motorista\n")
            if op=='a':
                cad_motorista()
                cont_mot=1
            if op=='b':
                if cont_mot!=0:
                    cpf=input("informe o cpf do motorista que deseja buscar")
                    moto=pesquisar_motorista(cpf)
                    print(moto)
                
            if op=='c':
                if cont_mot!=0:
                    cpf=input("informe o cpf do motorista que deseja buscar")
                    moto=pesquisar_motorista(cpf)
                    editar_motorista(moto)
            if op=='d':
                if cont_mot!=0:
                    cpf=input("informe o cpf do motorista que deseja buscar")
                    moto=pesquisar_motorista(cpf)
                    deletar_motorista(moto)
            
            pass
        if opcao == 2:
            op=input("a-Cadastrar Novo veiculo\n"
        "b-Pesquisar veiculo\n"
        "c-Editar veiculo\n"
        "d-Deletar veiculo\n")
                
            if op=='a':
                    cad_veiculos()
                    cont_veiculos=1
                    pass
            if op=='b':
                if cont_veiculos!=0:
                    placa=input("informe a placa do veiculo que deseja buscar")
                    veiculo=pesquisar_veiculos(placa)
                    print(veiculo)

                    pass
        
            if op=='c':
                if cont_veiculos!=0:
                    placa=input("informe a placa do veiculo que deseja buscar")
                    veiculo=pesquisar_veiculos(placa)
                    editar_veiculos(veiculo)
                    pass
            if op=='d':
                if cont_veiculos!=0:
                    placa=input("informe a placa do veiculo que deseja buscar")
                    veiculo=pesquisar_veiculos(placa)
                    deletar_veiculo(veiculo)
                    pass
            if op=='e':
                if cont_veiculos!=0:
                    placa=input("informe a placa do veiculo que deseja buscar")
                    veiculo=pesquisar_veiculos(placa)
                    quilometragem(veiculo)
                    pass
            
    
            pass
        if opcao == 3:
            op=(input("a-Cadastrar Viagem\n"

"b-Editar Viagem\n"))
            

            if op=='a':
             if (cont_mot or cont_veiculos)!=0:
                cad_viagem()
                dados+=1
            pass
            
            if op=='b':
              if (cont_mot or cont_veiculos)!=0:
                cod_v=int(input('informe o código da viagem'))
                editar_viagem(cod_v)
             
                   
            pass
        if opcao == 4:
                abastecimento()
                cod_abastec+=1
        pass
        if opcao == 5:
                manutencao()
                cod_manutencao+=1
        pass
        if opcao == 6:
           
           pass
    

           
def cad_motorista():
    nome = input('Digite seu nome:')
    cpf = input('Insira seu CPF:')  
    rg=input('informe seu rg')
    cnh=input('informe sua cnh') 

    motorista={
        "NOME":nome,"CPF":cpf,"RG":rg,"CNH":cnh
    }
    motoristas[cpf]=motorista 
    print(motoristas)

def pesquisar_motorista(cpf):
    motorista= motoristas.get(cpf)
    if motorista:
        return motorista
    else:
        print("não existe")
        
def editar_motorista(motorista):

    if motorista:
            nome = input('Digite seu nome:')
            cpf = input('Insira seu CPF:')  
            rg=input('informe seu rg')
            cnh=input('informe sua cnh') 
            motorista={
        "NOME":nome,"CPF":cpf,"RG":rg,"CNH":cnh
    }
    motoristas[cpf]=motorista 
            
    print('Seus dados foram atualizados ;)')

def deletar_motorista(motorista):
    cpf=motorista["CPF"]
    del motoristas[cpf]
    print('motorista deletado')
           
def cad_veiculos():
    marca = input('Digite seu nome:')
    modelo= input('Insira seu CPF:')  
    placa=input('informe seu rg')
    chassi=input('informe sua cnh') 
    cor=input('informe a cor do veiculo')
    km=input('Quilometros rodados')
    veiculo={
        "marca":marca,"modelo":modelo,"placa":placa,"chassi":chassi,"cor":cor,"km":km
    }
    veiculos[placa]=veiculo

def pesquisar_veiculos(placa):
    veiculo= veiculos.get(placa)
    if veiculo:
        return veiculo
    else:
        print("não existe")
        
def editar_veiculos(veiculo):

    marca = input('Digite a marca do veiculo:')
    modelo= input('Insira seu CPF:')  
    placa=input('informe seu rg')
    chassi=input('informe sua cnh') 
    cor=input('informe a cor do veiculo')
    km=input('Quilometros rodados')
    veiculo={
        "marca":marca,"modelo":modelo,"placa":placa,"chassi":chassi,"cor":cor,"km":km
    }
    veiculos[placa]=veiculo
            
def deletar_veiculo(veiculo):
     placa=veiculo["placa"]
     del veiculos[placa]
     print('veiculo deletado')

def quilometragem(veiculo):
    km=veiculo["km"]
    print(veiculos[km])

def cad_viagem():
    destino = input('Digite o destino:')
    origem= input('digite a origem:')  
    distancia=input('distancia da viagem') 
    cpf=input("cpf do motorista que realizou a viagem")
    motorista=pesquisar_motorista(cpf)
    placa=input("informe a placa do carro que realizou a viagem")
    veiculo=pesquisar_veiculos(placa)
    viagem_dados={
        "destino":destino,"origem":origem,"motorista":motorista,"distancia":distancia,"veiculo":veiculo
    }
    viagens[dados]=viagem_dados
    print(dados)

def editar_viagem(codigo):
     codigo_viagem=viagens.get(codigo)
     if codigo_viagem:
            destino = input('Digite seu nome:')
            origem= input('Insira seu CPF:')  
            distancia=input('informe sua cnh') 
            cpf=input("cpf do motorista que realizou a viagem")
            motorista=pesquisar_motorista(cpf)
            placa=input("informe a placa do carro que realizou a viagem")
            veiculo=pesquisar_veiculos(placa)
            viagem_dados={
                "destino":destino,"origem":origem,"motorista":motorista,"distancia":distancia,"veiculo":veiculo
                
            }
            viagens[dados]=viagem_dados 

def manutencao():
    data=input("informe a data")
    tipo=input("informe o  tipo da viagem")
    valor=input("informe o valor")
    placa=input("informe a placa do carro que abasteceu")
    veiculo=pesquisar_veiculos(placa)
    manutencao={
       "veiculo":veiculo,"data":data,"tipo":tipo,"valor":valor
    }
    manutencoes[cod_manutencao]=manutencao
    print("codigo de manutenção",cod_manutencao)

def abastecimento():

    valor=input("informe o valor do abastecimento")
    data=input("informe a data do abastecimento")
    quantidade=input("informe a quantidade de abastecimento")
    placa=input("informe a placa do carro que abasteceu")
    veiculo=pesquisar_veiculos(placa)

    abastec={
        "veiculo":veiculo,"valor":valor,"data":data,"quantidade":quantidade
    }
    abastecimentos[cod_abastec]=abastec
    print("codigo de abastecimento",cod_abastec)


def relatorio():
   
    print("Quantidade de motoristas",len(motoristas))
    
    print("Quantidade de veiculos",len(veiculos))

menu()