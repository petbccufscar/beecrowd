#include <stdio.h>

int main()
{

    int N, v, i, soma;

    while (scanf("%i", &N) != EOF)
    {
        soma = 0;
        for (i = 0; i < N; i++)
        {
            scanf("%i", &v);
            soma += v;
        }
        if (soma >= (N / (3 * 1.0f)) * 2)
        {
            printf("impeachment\n");
        }
        else
        {
            printf("acusacao arquivada\n");
        }
    }
    return 0;
}