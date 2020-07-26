#include <stdio.h>

int main()
{
    int num, cont;
    scanf("%d", &num);
    for (cont = 2; cont <= num; cont += 2)
    {
        printf("%d^2 = %d\n", cont, (cont * cont));
    }
    return 0;
}