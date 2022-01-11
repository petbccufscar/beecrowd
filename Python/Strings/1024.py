# Problema 1024 - Beecrowd - Strings - Nível 5

# Entrada da quantidade de casos teste
qtdTestes = int(input())

# Recebimento das strings para codificação.
for i in range(qtdTestes):
    msg = input()
    msgCriptografada = ""

    # Primeira passada: Todas letras irão andar 2 casas para a direita na tabela ASCII.
    for letra in msg:

        # A métodos ".isalpha()" verifica se o caractere é uma letra ou não.
        if letra.isalpha():

            # A função "ord()" transforma um caractere em seu número ASCII, e a função "chr()".
            # tranforma um número em caractere.
            msgCriptografada += chr(ord(letra) + 3)

        # Caso não seja uma letra
        else:
            msgCriptografada += letra

    # Segunda passada: Deve inverter a string.
    msgCriptografada = msgCriptografada[::-1]

    # Terceira passada: Voltar uma casa na tabela ASCII a última metade da mensagem criptografada.

    # Faz com que a segunda metade da mensagem criptografada esteja no auxiliar que será usado no for abaixo.
    aux = msgCriptografada[int(len(msgCriptografada) / 2) :]

    # Guarda a primeira metade da mensagem criptografada na própria mensagem criptografada.
    msgCriptografada = msgCriptografada[: int(len(msgCriptografada) / 2)]

    for letra in aux:

        # Voltando uma casa na tabela ASCII de cada letra.
        msgCriptografada += chr(ord(letra) - 1)

    # Apresentação da resposta.
    print(msgCriptografada)
