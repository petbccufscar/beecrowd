# Problema 3140 - URI - Iniciante - Nível 1

# Flag para sinalizar que o programa está lendo uma linha dentro das tags
# <body> </body>, inicia-se com valor booleano False
dentro = False

# Laço que lê uma entrada até encontrar o fechamento de tag '</body>'
while True:
    # Leitura da linha na entrada de dados
    linha = input()
    # Se existe a tag '<body>' na linha em questão
    if '<body>' in linha:
        # A flag dentro é alterada para o valor True
        dentro = True
        continue
    # Caso o fechamento de tag '</body>' seja encontrado dentro da linha
    elif '</body>' in linha:
        # O programa é finalizado
        exit()
    # Se a flag dentro for igual a True, a linha é exibida na saída de dados
    if dentro:
        print(linha)
