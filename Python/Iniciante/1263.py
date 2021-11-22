# Problema 1263 - Beecrowd - Iniciante - Nível 3

# Executa o loop enquanto a entrada padrão não indicar EOF
while True:
    try:
        # Variável que irá armazenar o texto informado
        texto = input();

        # Converte todos os caracteres para letras minúsculas
        texto = texto.lower();

        # Quantidade de aliterações na string
        aliteracoes = 0

        # Caractere da palavra predecessora
        caractere = '\0'

        # Contará quantas palavras, consecutivamente,
        # tem a mesma letra inicial
        contador = 0

        for i in texto.split():
            if i[0] == caractere:
                # Incrementa a quantidade de aliterações
                # somente se for a primeira palavra consecutiva
                # a anterior e desconsiderada se, nessa sequência,
                # aparecerem mais palavras com a mesma letra inicial
                if contador == 1:
                    aliteracoes += 1

                # Dado que o caractere é igual a
                # letra inicial da palavra anterior
                # incrementa o contador de palavras em sequência
                contador += 1
            else:
                # Dado que o caractere é diferente do que estava
                # armazenado na variável, a sequência é resetada
                # com o novo caractere
                caractere = i[0]

                # Reseta o contador e considera a primeira
                # palavra na sequência de palavras com mesma inicial
                contador = 1

        print(aliteracoes)
    except EOFError:
        break
