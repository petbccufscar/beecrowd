# Problema 1827 - URI - Iniciante - Nível 1

# Importando biblioteca sys
import sys
#Leitura dos tamanhos da matriz quadrada até o fim de arquivo
while tam := sys.stdin.readline():
    # Conversão do input de string para inteiro
    tam = int(tam)
    # Laço que vai até tam, representando cada linha da matriz a ser exibida na tela
    for i in range(tam):
        # Lista com quantidade tam de zeros
        linha = ['0']*tam
        # Condição que verifica se o i está no meio da matriz
        if i >= tam//3 and i < tam - tam//3:
            # Substituindo porção central da linha por vários números 1
            linha[tam//3:-(tam//3)] = ['1']*(tam - 2*(tam//3))
            # Se i corresponde à metade das linhas da matriz
            if i == tam//2:
                # Colocar número 4 na posição central da linha
                linha[i] = '4'
        # Caso i não represente as linhas centrais da matriz
        else:
            # Colocando número 2 na posição da linha de modo a prencher a
            # diagonal principal
            linha[i] = '2'
            # O mesmo é feito com o número 3 na diagonal secundária
            linha[tam-1-i] = '3'
        # Efetua-se um print da linha formatada de acordo com as condições anteriores
        print(''.join(linha))
    # Utilização de um print para pular linha entre as matrizes
    print('')
