#include <stdio.h>

int main()
{

    double A[100];
    int i;

    for(i=0; i<100; i++)
        scanf("%lf", &A[i]);

    for(i=0; i<100; i++)
    {

        if(A[i]<=10.0)
            printf("A[%d] = %.1lf\n",i, A[i]);

    }

    return 0;
}