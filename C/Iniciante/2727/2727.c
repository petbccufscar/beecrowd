#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main()
{
    int n, i, j, qtd, espaco;
    char *letra;
    char um[10] = {'a', 'd', 'g', 'j', 'm', 'p', 's', 'v', 'y', '\0'};
    char dois[10] = {'b', 'e', 'h', 'k', 'n', 'q', 't', 'w', 'z', '\0'};
    char tres[10] = {'c', 'f', 'i', 'l', 'o', 'r', 'u', 'x', '\0'};

    while ((scanf("%d", &n)) != EOF)
    {
        fflush(stdin);
        for (i = 0; i < n; i++)
        {
            qtd = 0;
            espaco = 0;
            letra = (char *)malloc(100 * sizeof(char));

            scanf("%[^\n]%*c", letra);

            for (j = 0; j < strlen(letra); j++)
            {
                if (letra[j] == ' ')
                {
                    espaco++;
                }
                else
                {
                    if (espaco == 0)
                    {
                        qtd++;
                    }
                }
            }

            if (qtd == 1)
                printf("%c\n", um[espaco]);
            else if (qtd == 2)
                printf("%c\n", dois[espaco]);
            else if (qtd == 3)
                printf("%c\n", tres[espaco]);

        }
    }

    return 0;
}