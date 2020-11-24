#include <stdio.h>
#include <string.h>

int main(){
    int i, j, tamanho;
    char palavra[110];
    
    while(scanf("%s",palavra) != EOF){

    tamanho = strlen(palavra);

    for(j = 0; j < strlen(palavra); j++){
        for(i=0;i<j;i++){
            printf(" ");
        }
        for(i = 0; i < tamanho-1 ;i++){
            printf("%c ",palavra[i]);
        }
        printf("%c",palavra[i]);
        tamanho--;
        printf("\n");
    }
    printf("\n");

    }
    return 0;
}