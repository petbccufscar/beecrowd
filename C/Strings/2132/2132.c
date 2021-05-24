#include <stdio.h>
#include <string.h>
#include <math.h>

int main()
{

    char palavra[61];
    int i, tam, caso = 1;
    long long int total;

    while (scanf("%s", palavra) != EOF)
    {
        printf("Palavra %i\n", caso);
        tam = strlen(palavra);
        total = 0;

        for (i = 0; i < tam; i++)
        {
            if (palavra[i] == 'b')
            {
                total = total + pow(2, tam - i - 1);
            }
        }

        printf("%lld\n\n", total);
        caso++;
    }

    return 0;
}