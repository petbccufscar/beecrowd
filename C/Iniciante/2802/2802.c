#include <stdio.h>

int main()
{

    long long N, resultado;
    scanf("%lli", &N);

    resultado = 1 + (((N - 1) * N) / 2) + ((N * (N - 1)*(N - 2)*(N - 3)) / 24);
    printf("%lli\n", resultado);

    return 0;
}