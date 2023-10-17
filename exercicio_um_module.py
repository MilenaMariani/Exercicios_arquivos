from ler_dados import ler_dados
from salvar_arquivos import criar_arquivo

if __name__ == '__main__':
    dados_alunos = ler_dados()
    criar_arquivo(dados_alunos = dados_alunos)
    