#include <stdio.h>
int main()
{
    double soma = 0.0, M[12][12];
    char O;
    int coluna, linha, contagem = 10;
    scanf("%s", &O);
    for (linha = 0; linha <= 11; linha++)
    {
        for (coluna = 0; coluna <= 11; coluna++)
            scanf("%lf", &M[linha][coluna]);
    }
    for (linha = 0; linha <= 10; linha++)
    {
        for (coluna = 0; coluna <= contagem; coluna++)
            soma += M[linha][coluna];
        contagem--;
    }
    if (O == 'S')
        printf("%.1lf\n", soma);
    else
    {
        printf("%.1lf\n", soma / 66.0);
    }
    return 0;
}