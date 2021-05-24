#include <stdio.h>

int main(){
    int X, i, soma;
    scanf("%d",&X);

    while(X != 0){
        soma = 0;
        for(i=0;i<5;i++){
            if(X%2 == 0){
                soma += X;
                X+=2;
            }
            else{
                soma += X + 1;
                X += 2;
            }
        }
        
        printf("%d\n",soma);
        scanf("%d",&X);
    }

    return 0;
}