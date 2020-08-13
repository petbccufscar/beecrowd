#include <stdio.h>
#include <string.h>

int main()
{
    int i, j, casos, contador, k, l;
    char subsq[100], seq[100];

    casos = 0;

    while(scanf("%s%s", subsq, seq)!=EOF)
    {
        int total, posicao, tmp, tam_subsq, tam_seq;

        tam_subsq = strlen(subsq); 
        tam_seq = strlen(str);
        
        total = 0;
        casos++;
        
        for(i=0; i <= tam_seq-tam_subsq; i++)
        {
            if(seq[i] == subsq[0])
            {
                contador = 1; 
                tmp = i + 1;
                
                for(k = i+1, l = 1; subsq[l]; l++, k++)
                {
                    if(seq[k] == subsq[l]) 
                        contador++;
                    else 
                        break;
                }
                if(contador == tam_subsq)
                {
                    total++;
                    posicao = tmp;
                }
            }
        }
        printf("Caso #%d:\n", casos);

        if(total == 0)
            printf("Nao existe subsequencia\n\n");
        else
        {
            printf("Qtd.Subsequencias: %d\n", total);
            printf("Pos: %d\n\n", posicao);
        }
    }
    return 0;
}