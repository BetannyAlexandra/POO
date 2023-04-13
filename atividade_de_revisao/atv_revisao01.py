# funcionarios = []
lista_telefone = []
opcao = 15
funcionarios = []


def menu():
    opcao = 15
    while opcao != 0:
        opcao = int(input("-----------MENU-----------\n"
                          "1. Cadastro de Funcionários\n"
                          "2. Pesquisar funcionário\n"
                          "3. Cadastrar novo telefone\n"
                          "4. Editar dados do Funcionário\n"
                          "5. Deletar funcionário\n"
                          "0.Sair\n"))
        if opcao == 1:
            cadastro()
            pass
        if opcao == 2:
            cpf = input('Informe o cpf para a busca:')
            buscar_cpf(cpf)
            pass
        if opcao == 3:
           cpf = input('Informe o cpf para cadastrar um novo telefone:')
           adc_tel(cpf)
           pass
        if opcao == 4:
           cpf = input('Informe o cpf para editar os dados do funcionario:')
           editar_dados(cpf)
           pass
        if opcao == 5:
            cpf = input('Informe o cpf para deletar funcionario:')
            deletar_funcionario(cpf)
            pass
        if opcao == 6:
           sair()
           pass
           
           

def cadastro():
    nome = input('Digite seu nome:')
    cpf = input('Insira seu CPF:')
    cargo = input('Informe seu cargo:')
    telefone = input('Insira seu telefone:')
    salario = input('Informe seu salario:')
  
    
    lista_telefone = telefone.split(",")

    cad = {"Nome": nome, "CPF": cpf, "Cargo": cargo, "Telefones": lista_telefone, "Salario": salario}

    funcionarios.append(cad)

def buscar_cpf(cpf):
    for busca in funcionarios:
        if busca["CPF"] == cpf:
            print('Funcionario encontrado')
            print(busca)

def adc_tel(cpf):
  telefone = input("Insira o telefone que deseja adionar:")
  for tele in funcionarios:
    if tele["CPF"] == cpf:
      tele["Telefones"].append(telefone)
      print('Foi adicionado um novo telefone')
      print(tele["Telefones"])

def editar_dados(cpf):
     for busca in funcionarios:
        if busca["CPF"] == cpf:
          nome = input('Digite seu nome:')
          cpf = input('Insira seu CPF:')
          cargo = input('Informe seu cargo:')
          telefone = input('Insira seu telefone:')
          salario = input('Informe seu salario:')

          cad = {"Nome": nome, "CPF": cpf, "Cargo": cargo, "Telefones": lista_telefone, "Salario": salario}

          funcionarios.append(cad)
          print('Seus dados foram atualizados ;)')
          return
        
def deletar_funcionario(cpf):
    for busca in funcionarios:
        if busca["CPF"] == cpf:
           funcionarios.remove(busca)
           print('Funcionario deletado')
           return
        
def sair():
     opcao == 0
   
        
                
menu()