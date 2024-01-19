# Problema 2003 - Beecrowd - Iniciante - Nível 2

# Criação do loop infinito enquanto o fim do arquivo (EOF) não for encontrado 
while True:
    try:
        # Lendo as variáveis 'hora' e 'minutos'
        hora, minutos = map(int, input().split(':'))

        # Calculadno os minutos totais gastos por Bino para chegar ao terminal
        minutos_totais = hora*60 + minutos + 60

        # Calculando o atraso máximo de Bino
        atraso_maximo = minutos_totais - 8*60
        
        # Caso Bino chege antes das 8h, seu atraso será zero
        if atraso_maximo < 0:
            print(f'Atraso maximo: 0')

        # Caso contrário, imprime seu atraso
        else:
            print(f'Atraso maximo: {atraso_maximo}')
    
    except EOFError:
        quit()