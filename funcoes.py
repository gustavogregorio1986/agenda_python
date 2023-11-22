def incluir(vetor):
    pessoa = {}
    pessoa['nome'] = input("Informe nome: ")
    pessoa['email'] = input("Informe email: ")
    pessoa['telefone'] = input("Informe telefone: ")

    vetor.append(pessoa)

def pesquisar(vetor, nomeBusca):
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