# Problema 1222 - URI - Strings - Nível 6

import math  

while True:
    try:
        # Leitura das variáveis
        n, l, c  = map(int,input().split(" "))
        # Quantidade de caracteres na linha atual
        caracteres = 0
        # Quantidade de linhas
        linhas = 1

        # Leitura do texto
        texto = input().split(" ")

        # Percorrendo cada palavra no texto
        for i in range(len(texto)):
            # Tamanho da palavra atual
            tam =  len(texto[i])

            # Se passou do limite de c caracteres por linha
            if ((caracteres + tam) > c):
                # Troca de linha
                linhas += 1
                caracteres = 0

            # Adicionando o tamanho da palavra + espaço no contador
            caracteres += tam + 1
                
        # Imprimindo a quantidade de páginas utilizada, usando a função "ceil(NUM)" para receber
        # o teto de um número, sendo: o menor inteiro, maior do que "NUM".
        print(math.ceil(linhas / (l)))
            

    except EOFError:
        break