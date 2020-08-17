#include <stdio.h>

int main()
{
    int N, i, j;
    char nome[20];
    double GD, pontuacao, max = 0.00, min = 10.00, soma = 0.00;
    scanf("%d", &N);
    for(i=1; i<=N; i++)
    {
        scanf("%s", nome);
        scanf("%lf", &GD);
        for(j=1; j<=7; j++)
        {
            scanf("%lf", &pontuacao);
            if(pontuacao > max) max = pontuacao;
            if(pontuacao < min) min = pontuacao;
            soma += pontuacao;
        }
        soma -= (max+min);
        soma *= GD;
        printf("%s %.2lf\n", nome, soma);
        max = 0.00, min = 10.00, soma = 0.00;
    }
    return 0;
}