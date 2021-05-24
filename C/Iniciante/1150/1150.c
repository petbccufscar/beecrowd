#include <stdio.h>
 
int main() {
 
    int X, Z, soma, res;
    
    res = 1;
    scanf("%d", &X);
    
    do {
        scanf("%d", &Z);
    } while (Z <= X);
 
    soma = X;
    
    while (soma <= Z) {
        X++;
        soma = soma + X;
        res++;
    }
    
    printf("%d\n", res);
    
    return 0;
}
