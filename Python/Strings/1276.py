alfabeto = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

while True:
    try:
				# Leitura da entrada com remoção dos espaços vazios
        texto = input().replace(' ', '')
        letras = []

				# Para cada posição da array texto é inserido seu valor na array 'letra', exceto se este valor já tiver sido inserido
        for letra in texto:
            try:
								# Procura se já esta no vetor letras
                letras.index(letra)
            except ValueError:
								# Caso não esteja é inserido
                letras.insert(len(letras), letra)
        
        faixas = []
				
				# Organização do vetor em ordem alfabética
        letras = sorted(letras)
        primeiraLetra = ''
        ultimaLetra = ''
        
        for letra in letras:
						# No primeiro loop atualiza o valor das variáveis 'primeiraLetra' e 'ultimaLetra'
            if primeiraLetra == '':
                primeiraLetra = letra
                ultimaLetra = letra
            else:
								# letra sempe está um valor a frete de 'ultimaletra', então caso sua posição no alfabeto for igual à posição 'ultimaletra'+1, significa que está em ordem alfabética, e portanto 'ultimaletra' é atualizado
                if alfabeto.index(letra) == alfabeto.index(ultimaLetra) + 1:
                    ultimaLetra = letra
                else:
										# Caso não esteja em ordem alfabética, a faixa de letras é inserido no vetor 'faixas' 
                    faixas.insert(len(faixas), primeiraLetra + ':' + ultimaLetra)
                    primeiraLetra = letra
                    ultimaLetra = letra

				# Inserindo os últimos valores no vetor						
        if primeiraLetra and ultimaLetra:
            faixas.insert(len(faixas), primeiraLetra + ':' + ultimaLetra)
        elif primeiraLetra and ultimaLetra == '':
            faixas.insert(len(faixas), primeiraLetra + ':' + ultimaLetra)

				
        textoFinal = ''

				# Armazena os valores das faixas em 'textoFinal'
        for faixa in faixas:
            textoFinal += faixa + ', '
					
        # Imprime o texto final sem ', ' final
        print(textoFinal[0: len(textoFinal) - 2])
    except EOFError:
        break