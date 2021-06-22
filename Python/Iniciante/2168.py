# Problema 2168 - URI - Iniciante - Nível 1

# Função que recebe as posições dos blocos e a matriz de câmeras
# Ela soma as câmeras dos quatros cantos dos blocos,
#   se tiver mais que uma câmera, o local é seguro 
def is_safe(x,y,m):
    sum = m[x][y] + m[x][y+1] +m[x+1][y] + m[x+1][y+1]
    return sum >= 2

# Leitura do N que decidirá o tamanho da matriz
n = int(input())
# Inicialização da matriz
matriz = []

# Leitura de cada linha da entrada
for i in range(n + 1):
    # Leitura da linha da entrada
    matriz.append(list(map(int, input().split(' '))))

for i in range(n):
    for j in range(n):
        # Verifica o bloco selecionado e imprime se é seguro ou não
        # O parâmetro end é usado para a customização do final da impressão
        # Assim, sobrescrevendo o final com quebra de linha
        print('S' if is_safe(i, j, matriz) else 'U', end='')
    # Imprime uma quebra de linha
    print()

