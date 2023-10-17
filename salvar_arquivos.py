def criar_arquivo(dados_alunos):
    """Cria um arquivo com os dados de um aluno """
    with open ("alunos.txt","w") as arquivo:
        for chave, valor in dados_alunos.items():
            linha = f'{chave}:{valor}\n'
            arquivo.write(linha) 

def criar_arquivo_lista(lista, nome_arquivo):
    """Cria um arquivo com os dados de uma lista de alunos """
    with open (nome_arquivo,"w") as arquivo:
        for item_lista in lista:
            for chave, valor in item_lista.items():
                linha = f'{chave}:{valor}\n'
                arquivo.write(linha) 
    