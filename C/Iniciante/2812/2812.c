#include <stdio.h>
#include <string.h>

int main()
{
    int i, j, a;
    int n, tam;
    int indice = 0, elem;

    scanf("%d", &n);

    for (a = 0; a < n; a++)
    {

        scanf("%d", &tam);
        int v[tam];

        for (i = 0; i < tam; i++)
        {
            scanf("%d", &elem);
            if (elem % 2 == 1)
            {
                v[indice] = elem;
                indice++;
            }
        }
        if (indice > 0)
        {

            int aux;
            for (i = 0; i < indice; i++)
            {
                for (j = i + 1; j < indice; j++)
                {
                    if (v[i] < v[j])
                    {
                        aux = v[i];
                        v[i] = v[j];
                        v[j] = aux;
                    }
                }
            }

            int maior = 0, menor = indice - 1;
            int resultado[indice];
            i = 0;

            while (maior <= (indice / 2))
            {
                resultado[i] = v[maior];
                resultado[i + 1] = v[menor];
                i += 2;
                maior++;
                menor--;
            }

            for (i = 0; i < indice; i++)
            {
                if (i == indice - 1)
                    printf("%d\n", resultado[indice - 1]);
                else
                    printf("%d ", resultado[i]);
            }

            indice = 0;
            memset(v, 0, sizeof(v));
            memset(resultado, 0, sizeof(resultado));
        }
        else
            printf("\n");
    }
    

    return 0;
}