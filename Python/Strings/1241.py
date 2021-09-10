# Problema 1241 - URI - Strings - Nível 2

# Inicialmente, recebemos o valor da quantidade de casos
casos = int(input())

# Em cada caso:
for _ in range(casos):
    # Recebemos os valores de entrada mantendo-os em string
    # pois não se faz necessária a conversão
    valorA, valorB, *_ = input().split(' ')

    # Se o segundo valor for maior que o primeiro, não há como encaixar
    if (len(valorB) > len(valorA)):
        print('nao encaixa')
        
    # Caso passe pela primeira verificação:
    else:
        # Utilizamos um loop paralelo, indo do final do vetor até o início.
        for x, y in zip(reversed(valorA), reversed(valorB)):
            # Caso algum dos digitos finais sejam diferentes, a verificação é interrompida
            if (x != y):
                print('nao encaixa')
                break
        # Caso o loop termine, a verificação foi conclúida e o valor encaixa
        else:
            print('encaixa')
