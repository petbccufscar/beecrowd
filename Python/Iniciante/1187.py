# Problema 1187 - Beecrowd - Iniciante - Nível 3

# Leitura do caractere inicial que indica soma ('S') ou multiplicação ('M')
c=input()

# Vetor 'm' para a leitura dos valores da matriz
m=[] 

# Leitura dos valores da matriz e seu armazenamento no vetor 'm'
for i in range(12):
    n = []
    for j in range (12):
        n.append(float(input()))
    m.append(n)

# Declaração das variáveis 'soma' e 'n'
soma=0
n=1

# Soma da área superior da matriz
for i in range(5):
    for j in range(n,12-n):
        soma=soma+m[i][j]
    n+=1

# Imprimindo a soma caso a variável 'c' for igual a 'S'
if c=='S':
    print(f'{soma:.1f}')

# Calculando e imprimindo a média caso a variável 'c' for igual a 'M'
elif c=='M':
    media=soma/30
    print(f'{media:.1f}')