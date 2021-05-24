#include <stdio.h>

int main()
{
    int T;

    scanf("%d", &T);

while (T) {
        char stringA[10001], *p1;
        char stringB[10001], *p2;
        int operacoes = 0;

        scanf("%s%s", stringA, stringB);

        for (p1 = stringA, p2 = stringB; *p1 != '\0'; ++p1, ++p2) {
            if (*p2 >= *p1)
                operacoes += *p2 - *p1;
            else
                operacoes += ('z' - *p1) + (*p2 - 'a') + 1;
        }

        printf("%d\n", operacoes);

        --T;
    }

    return 0;
}