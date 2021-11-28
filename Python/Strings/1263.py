# Problema 1263 - Beecrowd - Iniciante - Nível 3

# Executa o loop enquanto a entrada padrão não indicar EOF
while True:
    try:
        # Variável que irá armazenar o texto informado
        texto = input();

        # Converte todos os caracteres para letras minúsculas
        texto = texto.lower();

        # Separamos cada palavra da linha
        palavras = texto.split(' ')
        
        # Agora pegamos só as primeiras letras
        letras = map(lambda p : p[0], palavras)
        
        # Quantidade de aliterações na string
        aliteracoes = 0

        # Caractere da palavra predecessora
        caractere = '\0'

        # Contará quantas letras consecutivamente iguais
        contador = 0

        for letra in letras:
            if letra == caractere:
                # Incrementa a quantidade de aliterações
                # somente se for a primeira letra consecutiva
                # a anterior e desconsiderada se, nessa sequência,
                # aparecerem mais letras iguais
                if contador == 1:
                    aliteracoes += 1

                # Dado que o caractere é igual a letra
                # incrementa o contador de palavras em sequência
                contador += 1
            else:
                # Dado que o caractere é diferente do que estava
                # armazenado na variável, a sequência é resetada
                # com o novo caractere
                caractere = letra

                # Reseta o contador e considera a primeira
                # palavra na sequência de palavras com mesma inicial
                contador = 1

        print(aliteracoes)
    except EOFError:
        break
