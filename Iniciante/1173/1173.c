 #include <stdio.h>

int main()
{
    int n[10], i, v;

    scanf("%d", &v);
    
    for(i=0; i<=9; i++)
    {
        n[i]=v;

        printf("N[%d] = %d\n",i,v);

        v=v*2;
    }
    return 0;
}