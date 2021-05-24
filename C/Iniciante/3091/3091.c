#include <stdio.h>

int main() {
    int dividendo, divisor, resto;
    scanf("%d %d", &dividendo, &divisor);
    resto = dividendo % divisor;
    printf("%d\n", resto);
    return 0;
}