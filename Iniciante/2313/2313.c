#include <stdio.h>

int max(int num1, int num2)
{
    return (num1 > num2) ? num1 : num2;
}

int min(int num1, int num2)
{
    return (num1 < num2) ? num1 : num2;
}

int main()
{
    long long int A, B, C, maior, intermediario, menor;
    scanf("%lld %lld %lld", &A, &B, &C);
    maior = max(A, max(B, C));
    menor = min(A, min(B, C));
    intermediario = A + B + C - maior - menor;
    if (maior >= intermediario + menor)
        printf("Invalido\n");
    else
    {
        if (maior == intermediario && intermediario == menor)
            printf("Valido-Equilatero\n");
        else if (maior != intermediario && intermediario != menor && maior != menor)
            printf("Valido-Escaleno\n");
        else
            printf("Valido-Isoceles\n");
        if (maior * maior == 
           (intermediario * intermediario + menor * menor))
            printf("Retangulo: S\n");
        else
            printf("Retangulo: N\n");
    }
    return 0;
}