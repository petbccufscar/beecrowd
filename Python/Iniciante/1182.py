#Problema 1182 - Beecrowd - Iniciante - Nível 2

#Declaração da função que cria matrizes
def criaMatriz():
    '''
    Neste caso vamos usar um gerador de vetores para criar a matriz do tamanho desejado
    Cada gerador preenche o vetor com o elemento que está antes dele, ou seja, quando fazemos "X for i in range(a)" ele preenche a matriz com "a" elementos "Xs"
    Geradores podem ser combinados para criar matrizes, para isso basta colocar outro gerador no posição de "X" que ele criará "a" geradores de vetores
    '''
    matriz = [[0 for i in range(12)] for j in range(12)]
    return matriz

#Declaração da função que lê os valores para preencher a matriz
def preencheMatriz(matriz):
    #Aqui usa-se dois loops aninhados, na qual o loop "i" percorre as linhas e o loop "j" percorre as colunas
    for i in range(12):
        for j in range(12):
            #Leitura dos dados de preenchimento da matriz
            matriz[i][j] = float(input())
    
#declaração da funcao que soma uma coluna
def soma(matriz, coluna):
    total = 0
    for i in range(12):
        total += matriz[i][coluna]
    return total

#Declaração da funcao média
def media(matriz, coluna):
    return soma(matriz, coluna) / 12


'''Programa principal'''
#Leitura de C
C = int(input())

#leitura de T
T = input()

#Declaração, criação e preenchimento da matriz
M = criaMatriz()
preencheMatriz(M)

#Decisão de qual operação fazer e output do resultado
if T == 'S':
    print(f"{soma(M, C):.1f}")

elif T == 'M':
    print(f"{media(M, C):.1f}")