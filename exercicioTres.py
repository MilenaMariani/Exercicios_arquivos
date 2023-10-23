import ast

def atualizarAluno(aluno_escolhido):
    escolha_atualizar = int(input("Digite 1 para atualizar o nome \nDigite 2 para atualizar a idade \nDigite 3 para atualizar o curso\n"))

    with open('manipulaçãoDeArquivos/listaExerciciosManipulacao/alunos.txt', 'r') as lista_alunos:
        for linha in lista_alunos:
            if aluno_escolhido in linha:

                teste = ast.literal_eval(linha)

                if (escolha_atualizar == 1):
                    teste["nome"] = input("Digite o novo nome: ")
                elif (escolha_atualizar == 2):
                    teste["idade"] = input("Digite a nova idade: ")
                elif (escolha_atualizar == 3):
                    teste["curso"] = input("Digite o novo curso: ")

                return teste
            