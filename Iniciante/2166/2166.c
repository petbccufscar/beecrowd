#include <stdio.h>


int main()
{
    double n, raiz;

    raiz = 0.0;

    scanf("%lf", &n);

    while(n>0)
    {
        raiz = raiz + 2.0;
        raiz = 1/raiz;
        n--;
    }

    raiz = raiz + 1.0;
    
    printf("%.10lf\n", raiz);
    
    return 0;
}