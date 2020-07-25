#include <stdio.h>

int main()
{   
    int M, N, i, Sum = 0, aux = 0;
    
    scanf("%d %d", &M, &N);
    
    if(M<=0||N<=0){
        return 0;    
    }

    if(M<N){
        aux = N;
        N = M;
        M = aux;
    }

    for(i= N; i<=M; i++){
            Sum = i + Sum;
            printf("%i ", i);
    }
    printf("Sum=%d\n", Sum);
    
    Sum = 0;
 
    while(M>0&&N>0){
        scanf("%d %d", &M, &N);
        if(M<N){
            aux = N;
            N = M;
            M = aux;
        }
        if(M>0&&N>0&&M!=0&&N!=0){     
            for(i= N; i<=M; i++){
                Sum = i + Sum;
                printf("%i ", i);
            }
            printf("Sum=%d\n", Sum);
            Sum = 0;
        }
    }
    
    return 0;
}