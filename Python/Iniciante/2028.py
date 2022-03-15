# Problema 2028 - Beecrowd - Iniciante - Nível 5

# Contador que identifica o número do caso
cont = 1
while True:
    try:
        
        # Leitura de um valor N inteiro
        N = int(input())
        
        # 'valores' representa a quantidade de valores em uma sequência e inicia com o valor 1, pois 0 sempre está em uma sequência
        valores = 1                 
        
        # 'seq' representa a sequência a ser montada e inicia com '0 ', pois todas as sequências possíveis possuem 0
        seq = '0 '                  
        
        # Loop que realiza o cálculo da quantidade de valores que a sequência possui
        # e realiza a montagem da sequência 
        for i in range(1, N+1):
            valores += i
            seq += (str(i) + ' ') * i
            
        # Caso a entrada N possua valor 0, imprimir na tela a frase referente ao caso com a palavra 'numero' no SINGULAR
        # Caso contrário, imprimir na tela a frase referente ao caso com a palavra 'numero' no PLURAL
        if N == 0:
            print(f'Caso {cont}: {valores} numero')
        else:
            print(f'Caso {cont}: {valores} numeros')
        
        # Imprimindo a sequência gerada, removendo o seu espaço sobrando no final da sequência utilizando a função rstrip()
        print(seq.rstrip(), end='\n\n')
        
        # Incrementando contador
        cont += 1
    except EOFError:
        break
        