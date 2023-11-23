from funcoes import incluir, pesquisar, listar, alterar, excluir


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
        else:
            print("contato não salvo")   
    elif opcao == 3:
        listar(agenda)
    elif opcao == 4:
        alterar(agenda)
    elif opcao == 5:
        excluir(agenda)
    elif opcao == 9:
        break
    else:
        print("Opção Invalida!")