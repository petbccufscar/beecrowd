# Problema 2157 - Beecrowd - Strings - Nível 1

# Recebendo o número de casos de teste.
numTestes = int(input())

for i in range(numTestes):

    # Recebendo valores de inicio e fim da sequência de números.
    inic, fim = map(int, input().split(" "))

    # Ordenando os valores caso o inicio seja maior que o fim.
    if inic > fim:
        aux = inic
        inic = fim
        fim = inic

    # Variável resultado guardará a sequência de números que é a resposta.
    resultado = ""

    # "for" loop para ir varrendo os números de "inic" ao "fim" colocando
    # na variável resultado os números em questão, sendo o fim do range "fim + 1"
    # para que o número "fim" esteja na lista também.
    for num in range(inic, fim + 1):
        resultado += str(num)

    # Ao final do loop, o resultado terá os valores de "inic" ao "fim", mas
    # é necessário inverter a string e adicioná-la no resultado para criar
    # uma sequência espelho, assim usa-se uma propriedade de listas para inverter
    # e adiciona essa string ao resultado.
    resultado += resultado[::-1]

    # Apresentação do resultado final.
    print(resultado)
