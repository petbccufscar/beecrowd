check = 0
while True:
    n = int(input())
    if n == 0:
        break
		# Imprimindo a linha branca entre os casos de teste
    if check==1:
      print()

    frases = []
    for i in range(n):
				# Leitura de cada frase concatenando os espaços vazios extras com um único ' ', armazenando o resultado no vetor 'l'
        frases.append(' '.join(input().split()))
		
		# Encontra o tamanho da maior palavra presente na array 'frases'
    m = max(len(i) for i in frases)
		
		# Imprime as palavras justificadas à margem direita
    for i in range(len(frases)):
				# Imprime o número de espaços vazios para a palavra ficar justificada à margem direita com a maior paladra da array
        for j in range(m-len(frases[i])):
            print('', end=' ')
				# Imprime a palavra
        print(frases[i])

    check = 1
