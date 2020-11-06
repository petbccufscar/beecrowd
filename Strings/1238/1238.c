#include <stdio.h>

int main()
{

    int i, j, tamanho1, tamanho2, maior, N;
    char string1[55], string2[55];
    scanf("%d", &N);
    for (i = 0; i < N; i++)
    {
        scanf("%s %s", &string1, &string2);
        tamanho1 = strlen(string1);
        tamanho2 = strlen(string2);
        if (tamanho1 < tamanho2)
            maior = tamanho2;
        else
            maior = tamanho1;
        for (j = 0; j < maior; j++)
        {
            if (j < tamanho1)
                printf("%c", string1[j]);
            if (j < tamanho2)
                printf("%c", string2[j]);
        }
        printf("\n");
    }
    return 0;
}
