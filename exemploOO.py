from modelos import Aluno, Curso

aluno = []

estudante = Aluno()
estudante.nome = "Juan"
estudante.email = "juan@teste.com"
estudante.nota1 = 8.0
estudante.nota2 = 6.5

estudante.endereco = "Rua 10"
print(estudante.endereco)
print(estudante.nome)

media = estudante.calcularMedia() 
print( media)

estudante.informarSituacao(media)

estudante2 = Aluno()
estudante2.nome = "Pedro"
estudante2.email = "pedro@teste.com"
estudante2.nota1 = 10.0
estudante2.nota2 = 8.0
#print(estudante2.endereco)
estudante.imprimirInformacoes()
estudante2.imprimirInformacoes()

aluno.append(estudante)
aluno.append(estudante2)

cursoword = Curso("Word", 100)



