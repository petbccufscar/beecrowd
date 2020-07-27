#include <stdio.h>
int main()
{
    double soma = 0.0, M[12][12];
    char T[2];
    int coluna, x, y, z, contagem = 1;
    scanf("%s", &T);
    for (x = 0; x <= 11; x++)
    {
        for (y = 0; y <= 11; y++)
            scanf("%lf", &M[x][y]);
    }
    for (z = 0; z <= 11; z++)
    {
        for (coluna = contagem; coluna <= 11; coluna++)
            soma += M[z][coluna];
        contagem++;
    }
    if (T[0] == 'S')
        printf("%.1lf\n", soma);
    else
    {
        printf("%.1lf\n", soma / 66.0);
    }
    return 0;
}