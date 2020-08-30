#include<stdio.h>

int main()
{
    int n, min, max, i;
    int altura, visitantes = 0;
    
    while (scanf ("%d %d %d", &n, &min, &max) != EOF)
    {
        for ( i = 0; i < n; i++)
        {
            scanf ("%d", &altura);
            if (altura >= min && altura <= max)
                visitantes++;
        }
        printf ("%d\n", visitantes);
        visitantes = 0;
    }
    return 0;
}