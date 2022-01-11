# Problema 1047 - Beecrowd - Iniciante - Nível 9

# Inicalmente, vamos ler os valores e salvar em variáveis
horaInicial, minutoInicial, horaFinal, minutoFinal = map(int, input().split(' '))

# Caso as horas de inicio e final sejam iguais
if horaInicial == horaFinal:

    # Caso os minutos de inicio e final sejam iguais
    if minutoInicial == minutoFinal:
        print(f'O JOGO DUROU 24 HORA(S) E 0 MINUTO(S)')
    
    # Caso os minutos de inicio sejam maiores que o final
    elif minutoInicial > minutoFinal:
        print(f'O JOGO DUROU 23 HORA(S) E {60 - (minutoInicial - minutoFinal)} MINUTO(S)')

    # Caso os minutos de inicio sejam menores que o final
    elif minutoInicial < minutoFinal:
        print(f'O JOGO DUROU 0 HORA(S) E {minutoFinal - minutoInicial} MINUTO(S)')

# Caso a hora de inicio seja maior que a final
elif horaInicial > horaFinal:

    # Caso os minutos de inicio e final sejam iguais
    if minutoInicial == minutoFinal:
        print(f'O JOGO DUROU {24 - (horaInicial - horaFinal)} HORA(S) E 0 MINUTO(S)')
    
    # Caso os minutos de inicio sejam maiores que o final
    elif minutoInicial > minutoFinal:
        print(f'O JOGO DUROU {23 - (horaInicial - horaFinal)} HORA(S) E {60 - (minutoInicial - minutoFinal)} MINUTO(S)')

    # Caso os minutos de inicio sejam menores que o final
    elif minutoInicial < minutoFinal:
        print(f'O JOGO DUROU {24 - (horaInicial - horaFinal)} HORA(S) E {minutoFinal - minutoInicial} MINUTO(S)')

# Caso a hora de inicio seja menor que a final
elif horaInicial < horaFinal:

    # Caso os minutos de inicio e final sejam iguais
    if minutoInicial == minutoFinal:
        print(f'O JOGO DUROU {horaFinal - horaInicial} HORA(S) E 0 MINUTO(S)')
    
    # Caso os minutos de inicio sejam maiores que o final
    elif minutoInicial > minutoFinal:
        print(f'O JOGO DUROU {horaFinal - horaInicial - 1} HORA(S) E {60 - (minutoInicial - minutoFinal)} MINUTO(S)')

    # Caso os minutos de inicio sejam menores que o final
    elif minutoInicial < minutoFinal:
        print(f'O JOGO DUROU {horaFinal - horaInicial} HORA(S) E {minutoFinal - minutoInicial} MINUTO(S)')