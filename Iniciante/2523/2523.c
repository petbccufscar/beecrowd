#include <stdio.h>

int main() {

    int tamanho = 0,posicao_letras, i = 0;
    char letras[25]; 
    while(scanf("%s", letras) != EOF) { 
        i = 0;
        scanf("%d", &tamanho);
        while (i < tamanho) {
            scanf("%d",&posicao_letras);
            printf("%c",letras[posicao_letras-1]);
            i++;
        }
        printf("\n");
    }
    return 0;
}   