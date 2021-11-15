# Problema 1607 - Beecrowd - Strings - Nível 2

# Entrada do número de testes que será feito.
numTestes = int(input())

# Vetor para armazenar as respostas para serem mostradas posteriormente.
respostas = []

# Recebendo as strings iniciais e finais, respectivamente pela função "input()"
# que será separada por " " e mapeada para as variáveis respectivas.
for i in range(numTestes):
    strInicial, strFinal = map(str, input().split(" "))
    avancos = 0

    # For loop para percorrer as strings e calcular a diferença entre as letras.
    for j in range(len(strInicial)):

        # Irá ser usado os valores da tabela ASCII dados pela função "ord()", e para saber quantas
        # letras devem ser avançadas faremos (letra final - letra inicial) % 26, pois o operador "%"
        # (resto) garante que depois da letra "z" vem a letra "a".
        avancos += (ord(strFinal[j]) - ord(strInicial[j])) % 26

    # Guarda o total de avanços no vetor "respostas".
    respostas.append(avancos)

# For loop para mostrar as respostas.
for i in range(numTestes):
    print(respostas[i])  