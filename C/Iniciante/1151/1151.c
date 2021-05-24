#include <stdio.h>
 
int main() {
 
    int i, aux1, aux2, N, x;
    aux1 = 0;
    aux2 = 1;
    
    scanf("%d", &N);
    
    switch (N) {
        case 1:
            printf("0\n");
        break;
        case 2:
            printf("0 1\n");
        break;
        default:
            printf("0 1 ");
            for (i=2;i<N-1;i++) {
                x = aux1 + aux2;
                aux1 = aux2;
                aux2 = x;
                printf("%d ", x);
            }
            x = aux1 + aux2;
            printf("%d\n", x);
    }
 
    return 0;
}
