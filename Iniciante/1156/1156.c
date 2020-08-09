#include <stdio.h>
#include <math.h>

int main() {

    double soma = 0, numerador = 1, n = 2, i = 0;

    while (numerador <= 39) {
        
        soma += numerador/pow(n, i);

        numerador += 2;
        i++;
    }
    
    printf("%.2f\n", soma);

    return 0;
}