# Problema 2157 - Beecrowd - Strings - Nível 1

# Recebendo o número de casos de teste.
numTestes = int(input())

for i in range(numTestes):

    # Recebendo valores de inicio e fim da sequência de números.
    inic, fim = map(int, input().split(" "))

    # Ordenando os valores caso o inicio seja maior que o fim.
    if inic > fim:
        inic, fim = fim, inic

# Conversão da lista, do "inic" até o "fim", para string
    resultado = "".join(map(range(inic, fim + 1)))
    # Ao final do loop, o resultado terá os valores de "inic" ao "fim", mas
    # é necessário inverter a string e adicioná-la no resultado para criar
    # uma sequência espelho, assim usa-se uma propriedade de listas para inverter
    # e adiciona essa string ao resultado.
    resultado += resultado[::-1]

    # Apresentação do resultado final.
    print(resultado)
