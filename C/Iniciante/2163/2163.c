#include <stdio.h>

int oitoVizinhos(int i, int j, int N, int M, int m[N][M])
{

    if ((m[i][j + 1] == 7 && m[i - 1][j + 1] == 7) && m[i + 1][j + 1] == 7)
    {
        if (m[i - 1][j - 1] == 7 && m[i][j - 1] == 7 && m[i + 1][j - 1] == 7)
        {
            if (m[i - 1][j] == 7 && m[i + 1][j] == 7)
            {
                return 1;
            }
        }
    }
    return 0;
}

int main()
{

    int N, M;
    int i, j, padrao = 0;
    
    scanf("%d %d", &N, &M);
    int padraoSabre[N][M];

    for (i = 0; i < N; i++)
    {
        for (j = 0; j < M; j++)
        {
            scanf("%d", &padraoSabre[i][j]);
        }
    }

    for (i = 1; i < N - 1; i++)
    {
        for (j = 1; j < M - 1; j++)
        {
            if (padraoSabre[i][j] == 42)
            {
                padrao = oitoVizinhos(i, j, N, M, padraoSabre);
                if (padrao == 1)
                {
                    printf("%d %d\n", i + 1, j + 1);
                    break;
                }
            }
        }
        if (padrao == 1)
            break;
    }

    if (padrao == 0)
        printf("0 0\n");

    return 0;
}