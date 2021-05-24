#include <stdio.h>
 
int main(){
 
    int N, matriz[70][70], i, j;
 
    while(scanf("%d", &N) != EOF){

        for(i = 0; i < N; i++){
            for(j = 0; j < N; j++) {
                if((i + j) == (N - 1)) {
                    matriz[i][j] = 2;
                } 
                else if (i == j){
                    matriz[i][j] = 1;
                }
                else {
                    matriz[i][j] = 3;
                }
            }
        }
 
        for(i = 0; i < N; i++){
            for(j = 0; j < N; j++) {
                printf("%d", matriz[i][j]);
            }
            printf("\n");
        }
    };

    return 0;
}