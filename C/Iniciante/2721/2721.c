#include <stdio.h>

int main()
{

    char *renas[] = {"Rudolph", "Dasher", "Dancer", "Prancer", "Vixen", "Comet", "Cupid", "Donner", "Blitzen"};
    int i, A, soma = 0;
    for (i = 0; i < 9; i++)
    {
        scanf("%d", &A);
        soma += A;
    }
    printf("%s\n", renas[soma % 9]);
    return 0;
}