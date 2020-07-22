#include <stdio.h>
int main() {
    float A, B, C, resultado;

    scanf("%f %f %f", &A, &B, &C);

    if ((A < (B + C)) &&
        (B < (A + C)) &&
        (C < (B + A))) {
        resultado = A + B + C;
        printf("Perimetro = %.1f\n", resultado);
    }
    else {
        resultado = ((A + B) * C) / 2;
        printf("Area = %.1f\n", resultado);
    }
    
    return 0;
}