#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main()
{
    char desenho[51][51], temp[51];
    int i, j, k, print;
    int N, M;
    int nova_altura, nova_largura;
    int proporcao_altura, proporcao_largura;

    while(scanf("%d %d", &N, &M), N)
    {
        for(i=0;i<N;i++){
           scanf("%s", desenho[i]);
        }
    
    scanf("%d %d", &nova_altura, &nova_largura);
    
    proporcao_altura = (nova_altura/N);
    proporcao_largura = (nova_largura/M);
    for(i=0;i<N;i++)
    {
        strcpy(temp, desenho[i]);
        for(j=0;j<proporcao_altura;j++)
        {
            for(k=0;k<strlen(temp);k++)
            {
                for(print=1;print<=proporcao_largura;print++)
                    printf("%c", temp[k]);
            }
            printf("\n");
        }

    }
    printf("\n");
	}
    return 0;
}