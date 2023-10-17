def ler_dados():
    """Ler dados de um aluno"""
    nome = input ("Digite o nome do aluno: ")
    idade = input ("Digite a idade do aluno: ")
    curso = input ("Digite o curso do aluno: ")

    dados_aluno = {
        "nome":nome,
        "idade":idade,
        "curso":curso,
    }
    return dados_aluno

def ler_varios_alunos():
    """Ler dados de vários alunos"""
    quantidade = int (input("Digite a Quantidade: "))
    alunos = []
    for x in range (0,quantidade):
        aluno = ler_dados()
        alunos.append (aluno)
    
    return alunos