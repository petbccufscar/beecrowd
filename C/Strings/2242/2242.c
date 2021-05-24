#include <stdio.h>
#include <stdlib.h>

int main () {
    char risada[100], risada_invertida[100];
    int i, j, comprimento;
    scanf("%s", &risada);
    comprimento = strlen(risada);
    for (i=0; i<comprimento; i++) {
        if ((risada[i] != 'a') && (risada[i] != 'e') && (risada[i] != 'i') && (risada[i] != 'o') && (risada[i] != 'u')) {
                for (j=i; j<(comprimento-1); j++) {
                    risada[j] = risada[j+1];
                }
                risada[comprimento-1] = '\0';
                comprimento--; 
                i--;
        }
    }
    j = 0;
    for(i=comprimento-1; i>=0; i--) {
        risada_invertida[j] = risada[i];
        j++;
    }
    risada_invertida[j] = '\0';
    if (strcmp(risada, risada_invertida)) {
        printf("N\n");
    }
    else {
        printf("S\n");
    }
    return 0;
}