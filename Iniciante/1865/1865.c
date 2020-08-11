#include <stdio.h>

int main()
{
    int C, contagem, newtons;
    char nome[10];
    scanf("%d", &C);
    for (contagem=1; contagem<=C; contagem++)
    {
        scanf("%s", nome);
        scanf("%d", &newtons);
        if (nome[0]=='T' && nome[1]=='h' && nome[2]=='o' && nome[3]=='r')
            printf("Y\n");
        else printf("N\n");
    }
    return 0;
}