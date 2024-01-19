# Problema 1848 - Beecrowd - Iniciante - Nível 3

# Contador de gritos
grito_cont = 0

# Valor previsto pelo corvo
valor_previsto = 0

# Loop responsável por calcular o resultado da loteria
while grito_cont < 3:
    
    # Leitura da entrada que representa a ação do corvo: grito ou piscada
    entrada = input()

    # Caso a entrada seja um grito ('caw caw')
    if entrada == 'caw caw':
        
        # Imprime o valor previsto
        print(valor_previsto)
        
        # Incrementando o contador de gritos
        grito_cont += 1
        
        # Zerando o valor_previsto para realizar o cálculo do próximo valor
        valor_previsto = 0
    else:
        
        # Criando variável que representa o valor do olho (mais significativo)
        valor_olho = 4
        
        # Para cada olho do corvo, calcular o valor previsto a partir dos olhos abertos
        for olho in entrada:
            if olho == '*':
                valor_previsto += valor_olho
            
            # Divide-se o valor do olho por 2 para obtermos o valor do próximo olho
            valor_olho //= 2

