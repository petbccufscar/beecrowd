#include <stdio.h>

int main()
{
    int N, X, cont;
    scanf("%d", &N);
    for (cont = 1; cont <= N; cont++)
    {
        scanf("%d", &X);
        if (X == 0)
            printf("NULL\n");
        else if (X <= 0 && X % 2 == 0)
            printf("EVEN NEGATIVE\n");
        else if (X <= 0 && X % 2 == -1)
            printf("ODD NEGATIVE\n");
        else if (X >= 0 && X % 2 == 0)
            printf("EVEN POSITIVE\n");
        else if (X >= 0 && X % 2 == 1)
            printf("ODD POSITIVE\n");
    }
    return 0;
}