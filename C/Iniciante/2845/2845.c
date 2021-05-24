#include <stdio.h>
 
int main() {
 
    int N, A[10000], maior, i;
    
    scanf("%d", &N);
    
    for (i=0;i<N;i++)
        scanf("%d", &A[i]);
        
    maior = A[0];
    
    for (i=0;i<N;i++)
        if (maior < A[i])
            maior = A[i];
            
    printf("%d\n", maior+1);
    
    return 0;
}
