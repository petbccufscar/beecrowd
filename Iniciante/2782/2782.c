#include <stdio.h>

int main() {

    int tamanho_sequencia = 1000, sequencia[tamanho_sequencia], escadinhas = 1, i;

    scanf("%d", &tamanho_sequencia);
    for (i = 0; i < tamanho_sequencia; i++) {
        scanf("%d", &sequencia[i]);
    }
    for (i = 0; i < (tamanho_sequencia - 2); i++) {
        if ( (sequencia[i] - sequencia [i + 1]) != (sequencia[i + 1] - sequencia[i + 2]) ) {
            escadinhas = escadinhas + 1;
        }
    }
    printf("%d\n", escadinhas);
    return 0;
}