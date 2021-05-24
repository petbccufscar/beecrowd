#include <stdio.h>
int main()
{
   int N[20], aux,i, j;
   
    for(i=0; i<20; i++)
        scanf("%d",&N[i]);

    j=19;
    for(i=0; i<10; i++)
    {
        aux=N[i];
        N[i]=N[j];
        N[j]=aux;
        j--;
    }

    for(i=0; i<20; i++)
        printf("N[%d] = %d\n",i,N[i]);

    return 0;
}
