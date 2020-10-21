#include <stdio.h>
 
int presente[20001];
 
int main() {
    int n, maior, menor, i;
    
    while (n != 0) {
        scanf("%d", &n);

        for(i = 0; i < 2*n; i++)
            scanf("%d", &presente[i]);
            
        maior = presente[0] + presente[2*n-1];
        menor = presente[0] + presente[2*n-1];
            
        for(i = 1; i < 2*n - 1; i++) {
            if (presente[i] + presente[2*n-1-i] > maior)
                maior = presente[i] + presente[2*n-1-i];
            if (presente[i] + presente[2*n-1-i] < menor)
                menor = presente[i] + presente[2*n-1-i];
        }
        
        if (n != 0)
            printf("%d %d\n", maior, menor);
    }
 
    return 0;
}
