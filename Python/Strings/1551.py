# Problema 1551 - Beecrowd - Strings - Nível 4

# Recebendo o número de frases que será testado
# e recebendo cada frase pelo loop for.
numFrases = int(input())

# Declarando uma lista de frases vazias ("") com o número de frases que será lidas.
frase = [""]*numFrases

for i in range(numFrases):
    frase[i] = input()

    # É necessário "limpar" a frase, pois iremos contar apenas as letras, assim é necessário
    # retirar as pontuções e espaços em branco com a propriedade ".replace()".
    frase[i] = frase[i].replace(" ", "")
    frase[i] = frase[i].replace(",", "")
    frase[i] = frase[i].replace(".", "")

for i in range(numFrases):
    # Um vetor de 26 posições nulas (0) para armazenar se uma letra foi usada ou não.
    # Em que a posição do vetor é relacionada com a letra do alfabeto, sendo a = 0, 
    # b = 1 e assim por diante. Se uma letra foi usada o posição do vetor será marcada como 1.
    letrasUsadas = [0]*26

    # Irá varrer toda a frase, receber o valor da tabela ASCII com a função "ord()", 
    # retirando 97 pois o "a" tem valor ASCII como 97, porém desejamos que ele seja 
    # a posição 0 do vetor e assim colocar 1 na posição correspondente da letra do vetor
    for letra in frase[i]:
        letrasUsadas[ord(letra)-97] = 1
    
    # Assim, após inserir 1 em cada posição de letra usada é possível contar o número de "1's",
    # com a propriedade ".count(valor_a_ser_contado)" do vetor e assim decidir a categoria da frase.
    if (letrasUsadas.count(1) == 26):
        print("frase completa")
    elif (letrasUsadas.count(1) >= 13):
        print("frase quase completa")
    else:
        print("frase mal elaborada")