#include <stdio.h>

int main()
{
    int nro, i;
    float raiz = 0.0;

    scanf("%d", &nro);

    for (i = 0; i < nro; i++)
    {
        raiz += 6.0;
        raiz = 1.0 / raiz;
    }
    raiz += 3.0;

    printf("%.10f\n", raiz);

    return 0;
}