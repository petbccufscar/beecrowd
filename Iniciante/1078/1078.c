#include <stdio.h>

int main()
{
    int N, cont, result;
    
    scanf("%d", &N);
    
    for(cont=1; cont<=10; cont++)
    {
        result = cont*N;
        printf("%d x %d = %d\n", cont, N, result);
    }
    
    return 0;
}