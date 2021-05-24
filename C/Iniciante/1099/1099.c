#include <stdio.h>
#include <stdlib.h>

int main() {

    int X, Y, N, aux, soma = 0;

    scanf("%d", &N);

    for (int i = 0; i < N; i++) {
        
        scanf("%d %d", &X, &Y);

        if (X > Y) {
            aux = X;
            X = Y;
            Y = aux;
        }

        soma = 0;

        for (X++; X < Y; X++) {
            if (X % 2 == 1) {
                soma = soma + X;
            }
        }

        printf("%d\n", soma);
    }

    return 0;
}

