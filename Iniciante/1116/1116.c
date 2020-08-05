#include <stdio.h>
 
int main() {
 
    int x, y, N, i;
    
    scanf("%d", &N);
 
    for(i=0;i<N;i++) {
        scanf("%d%d", &x, &y);
        if (y == 0)
            printf("divisao impossivel\n");
        else
            printf("%0.1lf\n", (double)x/y);
    }
    
    return 0;
}
