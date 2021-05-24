#include <stdio.h>
 
int main() {
 
    int a, b, fibo, k, vetor[1000000], aux, i;
 
    scanf("%d", &k);
    
    a = 2;
    b = 3;
    i = 0;
    
    while (i <= k-1) {
        fibo = a + b;
        a = b;
        b = fibo;
        
        if (b - a > 1) {
            aux = a + 1;
            while (aux < b) {
                vetor[i] = aux;
                aux++;
                i++;
            }
        }
    }

    printf("%d\n", vetor[k-1]);
    
    return 0;
}
