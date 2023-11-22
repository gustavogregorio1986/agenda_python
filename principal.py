from funcoes import incluir, pesquisar


def menu():
    print("1 - Cadastro")
    print("2 - Pesquisa pelo nome")
    print("3 - Listar")
    print("4 - Alterar")
    print("5 - Excluir")
    print("9 - sair")
agenda = []
while True:
    menu()
    opcao = int(input('Informe a opção: '))
   
    if opcao == 1:
       incluir(agenda)
    elif opcao == 2:
        nomeBusca = input('Informe o nome para busca: ')
        indice = pesquisar(agenda, nomeBusca)
        if indice != -1:
            print(f"""{agenda[indice]['nome']} - 
                     {agenda[indice]['email']} - 
                     {agenda[indice]['telefone']}""")   
    elif opcao == 3:
        for elemento in agenda:
            print(f"{elemento['nome']}\t{elemento['email']}\t{elemento['telefone']}")
    elif opcao == 4:
        nomeBusca = input('Informe o nome para busca: ')
        for elemento in agenda:
            posicao = posicao + 1
            if elemento['nome'].lower() == nomeBusca.lower():
               break

        if posicao != -1:
            agenda[posicao]['nome'] = input('Informe o nome: ')
            agenda[posicao]['email'] = input('Informe o email: ')
            agenda[posicao]['telefone'] = input('Informe o telefone: ')
    elif opcao == 5:
        nomeBusca = input('Informe o nome para busca: ')
        for elemento in agenda:
            posicao = posicao + 1
            if elemento['nome'].lower() == nomeBusca.lower():
               break
            if posicao != -1:
                agenda.pop(posicao)
    elif opcao == 9:
        break
    else:
        print("Opção Invalida!")