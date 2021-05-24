#include <stdio.h>
#include <string.h>

int main() {
    int n, contador, i, j;
    int alfabeto[26];
    char frase[1001];
 
    scanf("%d", &n);
    
    for(i = 0; i < 26; i++)
        alfabeto[i] = 0;
    
    for(i = 0; i < n; i++) {
        contador = 0;
        scanf(" %1001[^\n]", frase);
        
        for(j = 0; j < strlen(frase); j++) {
            if (frase[j] >= 'a' && frase[j] <= 'z')
                if (alfabeto[frase[j] - 'a'] == 0)
                    alfabeto[frase[j] - 'a'] = 1;
        }
        
        for(j = 0; j < 26; j++) {
            if (alfabeto[j] == 1) {
                contador++;
                alfabeto[j] = 0;
            }
        }
        
        if (contador < 13)
            printf("frase mal elaborada\n");
        else if (contador < 26)
            printf("frase quase completa\n");
        else
            printf("frase completa\n");
    }
    
    return 0;
}
