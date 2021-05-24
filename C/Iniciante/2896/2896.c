
#include <stdio.h>

void main ()
{
    int casos, i, compradas, troca;

    scanf("%d", &casos);

    while (casos--)
    {
        scanf("%d %d", &compradas, &troca);

        int contador = 0;

        for (i = compradas; i >= troca; i -= troca)
            contador++;

        printf("%d\n", contador + i);

    }

}