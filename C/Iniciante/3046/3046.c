#include <stdio.h>

int main () {
    int duplo_N, pecas_existentes;
    scanf("%d", &duplo_N);
    pecas_existentes = (((duplo_N + 1) * (duplo_N + 2)) / 2);
    printf("%d\n", pecas_existentes);
    return 0;
}