#include <stdio.h>
 
int main() {
 
    int i, x, N;

    scanf("%d", &N);
    
    x = N;
    for (i=1;i<N;i++)
        x = x * i;

    printf("%d\n", x);
    
    return 0;
}
