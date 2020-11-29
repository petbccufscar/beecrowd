#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main() {
 
    char frase[101], palavra[101];
    int maior, i;

    maior = 0;    
    do {
        int lista_palavra[50], num_palavras;
        scanf(" %101[^\n]", frase);

        lista_palavra[0] = 0;
        num_palavras = 1;
        
        if (frase[0] != '0') {
            for(i=0;i<strlen(frase);i++) {
                if (frase[i] == ' ') {
                    lista_palavra[num_palavras] = i;
                    num_palavras++;
                }
            }
            lista_palavra[num_palavras] = strlen(frase);
            
            if (lista_palavra[1] - lista_palavra[0] >= maior) {
                maior = lista_palavra[1] - lista_palavra[0];
                strncpy(palavra, frase + 0, maior);
            }
            printf("%d", lista_palavra[1] - lista_palavra[0]);
                       
            for(i = 2; i <= num_palavras; i++) {
                if (lista_palavra[i] - lista_palavra[i-1] - 1 >= maior) {
                    maior = lista_palavra[i] - lista_palavra[i-1] - 1;
                    strncpy(palavra, frase + lista_palavra[i-1]+1, maior);
                    palavra[maior] = '\0';
                }
                printf("-%d", lista_palavra[i] - lista_palavra[i-1] - 1);
            }
            printf("\n");
        }
        
    } while (frase[0] != '0');
    i = 0;
    printf("\nThe biggest word: ");
    while (palavra[i] >= 65 && palavra[i] <= 90 || palavra[i] >= 97 && palavra[i] <= 122) {
        printf("%c", palavra[i]);
        i++;
    }
    printf("\n");
    return 0;
}
