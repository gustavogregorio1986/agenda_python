def incluir(vetor):
    pessoa = {}
    pessoa['nome'] = input("Informe nome: ")
    pessoa['email'] = input("Informe email: ")
    pessoa['telefone'] = input("Informe telefone: ")

    vetor.append(pessoa)

def pesquisar(vetor, nomeBusca):
    posicao = -1
    econtrado = False
    for elemento in vetor:
        posicao = posicao + 1
        if elemento['nome'].lower() == nomeBusca.lower():
            encontrado = True
            break
        if encontrado:
            return posicao
        else:
            return -1
        

def listar(vetor):
   for elemento in vetor:
            print(f"{elemento['nome']}\t{elemento['email']}\t{elemento['telefone']}")

def alterar(vetor):
        posicao = posicao + 1
        if posicao != -1:
            vetor[posicao]['nome'] = input('Informe o nome: ')
            vetor[posicao]['email'] = input('Informe o email: ')
            vetor[posicao]['telefone'] = input('Informe o telefone: ')
        else:
            print("Contato não existe")

def excluir(vetor):
        nomeBusca = input('Informe o nome para busca: ')
        posicao = posicao + 1
        for elemento in vetor:
            if elemento['nome'].lower() == nomeBusca.lower():
               break
            if posicao != -1:
                vetor.pop(posicao)
            else:
                print("Contato não existe")
    