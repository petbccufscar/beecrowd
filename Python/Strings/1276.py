# Problema 1276 - Beecrowd - Strings - Nível 3

while True:
    try:
        # Leitura da entrada com remoção dos espaços vazios
        texto = input().replace(' ', '')
        
        # Vamos converter o texto em um conjunto, para eliminar as letras repetidas
        letras = set(texto)

        # Vamos converter o conjunto para uma lista ordenada
        letras = sorted(list(letras))

        # Se a entrada for vazia apenas printamos uma linha vazia
        if len(letras) == 0:
            print()
            continue

        # Para poder verificar ordem, vamos converter as letras em números
        numeros = list(map(ord, letras))

        # Definimos o inicío e o fim da sequência como o primeiro número
        inicio = numeros[0]
        fim = numeros[0]

        # Lista vazia de faixas
        faixas = []

        # Para cada número vemos se ele é a continuação do fim
        for n in numeros[1:]:
            # Se sim, incrementamos o fim
            if n == fim + 1:
                fim += 1
            # Se não, terminamos a faiza corrente e iniciamos uma nova com o novo valor
            else:
                faixas.append((inicio, fim))
                inicio = fim = n

        # Precisamos levar em conta a última faixa
        faixas.append((inicio, fim))

        # Como o padrão de saída requer que as faizas sejam separadas por virgula
        # Vamos converter cada faixa para a notação usada: a:b
        faixas = map(lambda f : f'{chr(f[0])}:{chr(f[1])}', faixas)
        
        # Então printar as faixar unidas por virgula
        print(', '.join(faixas))

    except EOFError:
        break