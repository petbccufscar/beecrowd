#include <stdio.h>

int main()
{
    int N, M, troco, i, contador;
    int possiveis[15] = {7, 12, 22, 52, 102, 15, 25, 55, 105, 30, 60, 110, 70, 120, 150};
    
    while(1)
    {
        scanf("%d%d", &N, &M);
        
        if(N==0 && M==0) 
            break;
        
        troco = M - N;
        
        for(i=0, contador = 0; i<15; i++)
        {
            if(possiveis[i] == troco)
            {
                contador = 1;
                break;
            }
        }
        if(contador) 
            printf("possible\n");
        else 
            printf("impossible\n");
    }
    return 0;
}