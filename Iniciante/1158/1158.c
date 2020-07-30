#include <stdio.h>

int main(){
    int N, i,j, X, Y, soma;
    scanf("%d",&N);

    for(i = 0; i < N; i++){
        scanf("%d %d",&X, &Y);
        soma = 0;
        for(j=0;j<Y;j++){
            if(X%2 == 1){
                soma += X;
                X+=2;
            }
            else{
                soma += X + 1;
                X += 2;
            }
        }
        printf("%d\n",soma);
    }

    return 0;
}