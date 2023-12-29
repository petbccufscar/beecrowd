def print_matrix(matrix):
    # Função para imprimir a matriz formatada com 'X' e 'O'
    for row in matrix:
        print(''.join(['O' if cell != 'X' else 'X' for cell in row]))
    print('@')

def main():
    while True:
        # Recebe o tamanho da matriz como entrada
        n = int(input())
        if n == 0:
            return  # Termina o programa se n for 0

        # Inicializa a matriz com 'O's
        matrix = [['O' for _ in range(n)] for _ in range(n)]

        # Inicializa as variáveis para rastrear a posição do 'X' na matriz
        lin, col = n // 2, n // 2 + 1
        i, j = n // 2, n // 2
        go = 0  # Direção inicial (0 - direita, 1 - cima, 2 - esquerda, 3 - baixo)
        k = 1   # Variável para controlar o deslocamento da espiral

        while True:
            # Coloca 'X' na posição atual e imprime a matriz
            matrix[i][j] = 'X'
            print_matrix(matrix)

            # Verifica se atingiu o final da espiral
            if i == n - 1 and j == n - 1:
                break

            # Coloca 'O' na posição atual
            matrix[i][j] = 'O'

            # Atualiza a posição com base na direção atual
            if go == 2:
                j -= 1
            elif go == 0:
                j += 1
            elif go == 1:
                i -= 1
            elif go == 3:
                i += 1

            # Verifica se é necessário mudar a direção
            if j == col and i == lin:
                if go == 0:
                    lin -= k
                    go = 1
                elif go == 1:
                    k += 1
                    col -= k
                    go = 2
                elif go == 2:
                    lin += k
                    go = 3
                elif go == 3:
                    k += 1
                    col += k
                    go = 0

        # Coloca 'O' na última posição da espiral
        matrix[i][j] = 'O'

# Chama a função principal quando o script é executado
if __name__ == "__main__":
    main()
