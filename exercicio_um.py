with open ('arquivo.txt', 'w') as arquivo:
    estudante = {}
    continuar = 1

    while continuar != 0:
        nome_estudante = (input("Digite o nome do estudante: "))
        idade_nome = (input("Digite a idade do estudante: "))     
        curso_estudante = (input("Digite o curso do estudante: "))

        estudante['nome'] = nome_estudante
        estudante['idade'] = idade_nome
        estudante['curso'] = curso_estudante

        arquivo.write (f"{estudante}\n")

        continuar = int (input("Digite 1 para continuar:\n Digite 0 para parar: "))
        
            

