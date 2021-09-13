#Problema 1305 - URI - String - Nível 3

import sys

# Função que lê uma linha e retorna um inteiro e a parte fracionária
def num(linha):
    try:
        inteira, fracionaria = linha.split(".")
        # Se na parte inteira não tiver nenhum número colocar um 0
        if inteira == "":
            inteira = "0"
        # Da mesma forma, coloca um 0 na parte fracionária se não houver nenhum
        # número após split
        if fracionaria == "":
            fracionaria = "0"
    # Caso o número seja apenas inteiro sem parte fracionária
    except ValueError:
        inteira = int(linha)
        fracionaria = '0'
    return int(inteira), float("0." + fracionaria)

# Função que converte a string de cutoff em um número de ponto flutuante
def cutoff(linha):
    return float(linha)

# Flag que será usada para alternar entre a leitura do número num e a string de
# cutoff
flag = "num"

# For que lê da entrada padrão
for linha in sys.stdin:
    # Remoção do caractere \n
    linha = linha.replace('\n', '')

    # Se a flag for igual a "num"
    if flag == "num":
        # Chamando a função num
        inteira, fracionaria = num(linha)
        # Alteração da flag para ler a string de cutoff
        flag = "cutoff"
    # Caso a flag seja igual a cutoff
    elif flag == "cutoff":
        # Chamando a função cutoff
        cutoff_num = cutoff(linha)
        # Alteração da flag para ler a string num
        flag = "num"
        # Se a parte fracionária é maior que o número de cutoff
        if fracionaria > cutoff_num:
            print(inteira + 1)
        # Caso contrário
        else:
            print(inteira)
