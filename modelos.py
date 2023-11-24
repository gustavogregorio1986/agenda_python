class Aluno:
    def __init__(self):
        self.nome = ''
        self.email = ''
        self.nota1 = 0.0
        self.nota2 = 0.0
    
    def imprimirInformacoes(self):
        print(f"""Nome: {self.nome} Email: {self.email} Nota1: {self.nota1} Nota2: {self.nota2}""")

    def calcularMedia(self):
        return (self.nota1 + self.nota2)/2
    
    def informarSituacao(self,calculo):
        if calculo >= 7.0:
            print("Aluno Aprovado")
        else:
            print("Aluno Reprovado")

    def incluir(vetor):
        aluno = {}
        aluno['nome'] = input("Informe o nome: ")
        aluno['nota1'] = input("Informe a nota1: ")
        aluno['nota2'] = input("Informe a nota2: ")

        vetor.append(aluno)
    def listar(vetor):
        for elemento in vetor:
             print(f"{elemento['nome']}\t{elemento['email']}\t{elemento['nota1']}\t{elemento['nota2']}")


class Curso:
    def __init__(self, c, v):
        self.nome = c
        self.valor = v