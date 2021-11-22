# Problema 1116 - Beecrowd - Iniciante - Nível 1
# Recebendo número de divisões na entrada de dados
N = int(input())

# For que repete N vezes
for i in range(N):
    # Aplicação da função float através do map na lista de dois valores (X, Y)
    X, Y = map(float, input().split(' '))
    # Caso Y não seja igual a 0, é possível efetuar a divisão
    if Y != 0:
        print(X/Y)
    # Caso contrário, mostrar na tela a mensagem "divisao impossivel"
    else:
        print('divisao impossivel')
