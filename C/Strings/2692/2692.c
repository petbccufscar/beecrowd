#include <stdio.h>
#include <stdlib.h>

int main() {
    int n, m, achou, i, j, k;
    char frase[1000];
    
    scanf("%d %d", &n, &m);
    
    char troca[2*n];
    
    for(i = 0; i < 2*n; i+= 2)
        scanf(" %c %c", &troca[i], &troca[i+1]);
        
    for(i = 0; i < m; i++) {
        scanf(" %1000[^\n]", frase);
        
        for(j = 0; j < strlen(frase); j++) {
            achou = 0;
            k = 0;
            while (achou == 0) {
                if (troca[k] == frase[j]) {
                    achou = 1;
                    if (k%2 == 0)
                        frase[j] = troca[k+1];
                    else
                        frase[j] = troca[k-1];
                }
                else if (k == 2*n-1)
                    achou = 1;
                k++;
            }
        }
        
        printf("%s\n", frase);
    }
    
    return 0;
}
