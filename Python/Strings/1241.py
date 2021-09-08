# Problema 1241 - URI - Strings - Nível 2

# Inicialmente, recebos o valor da quantidade de casos
casos = int(input())

# Em cada caso:
for _ in range(casos):
    # Recebemos os valores de entrada mantendo-os em string
    # pois não se faz necessária a conversão
    valor = list(input().split())

    # Se o segundo valor for maior que o primeiro, não há como encaixar
    if (len(valor[1]) > len(valor[0])):
        print('nao encaixa')
        
    # Caso passe pela primeira verificação:
    else:
        # Utilizamos um loop paralelo, com o range reverso, indo do final do vetor até o início.
        for x, y in zip(reversed(range(len(valor[0]))), reversed(range(len(valor[1])))):
            # Caso algum dos digitos finais sejam diferentes, a verificação é interrompida
            if (valor[0][x] != valor[1][y]):
                print('nao encaixa')
                break
        # Caso o loop termine, a verificação foi conclúida e o valor encaixa
        else:
            print('encaixa')
