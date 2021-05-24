#include <stdio.h>
#include <stdlib.h>

int main() {
 
    int n, i, j;
    char frase[101];
    
    scanf("%d", &n);
    
    for(i = 0; i < n; i++) {
        scanf(" %100[^\n]", frase);
        
        j = 0;
        while (j < strlen(frase) - 8) {
            if ((frase[j] == 'o') && (frase[j+1] == 'u') && (frase[j+2] == 'l') && (frase[j+3] == 'u')
            && (frase[j+4] == 'p') && (frase[j+5] == 'u') && (frase[j+6] == 'k') && (frase[j+7] == 'k')) {
                frase[j-1] = 'J';
                frase[j+8] = 'i';
            }
            j++;
        }
        
        printf("%s\n", frase);
    }
 
    return 0;
}
