#include <stdio.h>
 
int main() {
 
    int N, R[100], i;
    
    scanf("%d", &N);
    
    for(i=0;i<N;i++)
        scanf("%d", &R[i]);
    
    for(i=1;i<N;i++) {
        if (R[i-1] > R[i]) {
            printf("%d\n", i+1);
            return 0;
        }
    }
    printf("0\n");
 
    return 0;
}
