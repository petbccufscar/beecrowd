#include <stdio.h>

int main() {

    double soma = 0, n = 1;

    while (n <= 100) {
        
        soma += 1/n;
        n++;
    }
    
    printf("%.2f\n", soma);

    return 0;
}