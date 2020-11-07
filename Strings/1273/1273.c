#include <stdio.h>
#include <string.h>

int max(int a,int b){
    if(a>b)
        return a;
    else
        return b;
}

int main(){
    int N, i,maior_palavra = 0, j,t;
    char palavras[50][50];

    scanf("%d",&N);
    while(N != 0){
        
        maior_palavra = 0;

        for(i = 0; i < N; i++){
            scanf("%s",palavras[i]);
            maior_palavra = max(maior_palavra,strlen(palavras[i]));   
        }

        for(i = 0; i < N; i++){
            t = maior_palavra - strlen(palavras[i]);
           for(j=0;j<t;j++){
                printf(" ");
            }
            printf("%s\n",palavras[i]);
        } 
        scanf("%d",&N);
        if(N != 0)
        printf("\n");
        
    }
    
    return 0;

}