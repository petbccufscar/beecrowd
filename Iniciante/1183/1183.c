#include <stdio.h>
int main()
{
    double soma = 0.0, M[12][12];
    char O[2];
    int coluna, x, y, linha, contagem = 1;
    scanf("%s", &O);
    for (x = 0; x <= 11; x++)
    {
        for (y = 0; y <= 11; y++)
            scanf("%lf", &M[x][y]);
    }
    for (linha = 0; linha <= 11; linha++)
    {
        for (coluna = contagem; coluna <= 11; coluna++)
            soma += M[linha][coluna];
        contagem++;
    }
    if (O[0] == 'S')
        printf("%.1lf\n", soma);
    else
    {
        printf("%.1lf\n", soma / 66.0);
    }
    return 0;
}