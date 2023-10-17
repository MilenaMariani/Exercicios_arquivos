def ler_dados ():
   
    nome = (input("Digite o nome do estudante: "))
    idade = (input("Digite a idade do estudante: "))     
    curso = (input("Digite o curso do estudante: "))

    dados_alunos = {
        "nome":nome,
        "idade":idade,
        "curso":curso,
    }
    return dados_alunos

def criar_arquivo (dados_alunos):
        with open ("alunos.txt", "w") as arquivo:
             for chave, valor in dados_alunos.items():
                  linha = f'{chave}:{valor}\n'
                  arquivo.write(linha)

def ler_arquivos():
    with open ('alunos.txt', 'r') as arquivo:
        for linha in arquivo:
            print(linha)

if __name__ == '__main__':
        dados_alunos = ler_dados()
        criar_arquivo(dados_alunos = dados_alunos)
        ler_arquivos()

        
        
            

