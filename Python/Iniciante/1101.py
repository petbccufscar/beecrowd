# Problema 1101 - Beecrowd - Iniciante - Nível 4

# Recebendo os valores de entrada em uma mesma linha.
m, n = map(int, input().split(" "))

# Loop while para validar os valores de entrada e repetir o procedimento.
while m > 0 and n > 0:

    # Sendo que "m" seja o inicio da lista de número e "n" o valor final
    # é necessário ordenar os valores recebidos do usuário. Caso "n" seja,
    # menor que o "m", o valor entre eles é invertido.
    if n < m:
        aux = n
        n = m
        m = aux

    # Criação da lista resultado que contém os valores entre "m" e "n"
    # e uma variável que irá armazenar a string da lista de números
    # entre "m" e "n". OBS: É necessário que o final do range seja "n + 1"
    # para que inclua o "n" na lista.
    resultado = []
    strResultado = ""
    
    for i in range(m, n + 1, 1):
        resultado.append(i)

        # Armazenando o número e um espaço para o próximo número na string.
        strResultado += str(i) + " "

    # Apresentação do resultado final, com a função "sum()"
    # que calcula a soma de uma lista inteira.
    print(f"{strResultado}Sum={sum(resultado)}")

    # Entrada de novos valores para "m" e "n".
    m, n = map(int, input().split(" "))
