#include <stdio.h>

int ehPrimo(int numero) {
    int i;

    if ((numero > 2 && numero % 2 == 0) || numero == 1) {
        return 0;
    }

    for (i = 3; i < numero/2; i += 2) {
        if (numero % i == 0) {
            return 0;
        }
    }

    return 1;
}
 
int main() {
 
    int M, N, i, soma;
    int V[20];
    
    while (scanf("%d", &M) != EOF) {

        soma = 0;

        for (i = 0; i < M; i++) {
            scanf("%d", &V[i]);
        }

        scanf("%d", &N);

        for (i = M - 1; i >= 0; i -= N) {
            soma += V[i];
        }

        if (ehPrimo(soma) == 1) {
            printf("You’re a coastal aircraft, Robbie, a large silver aircraft.\n");
        } else {
            printf("Bad boy! I’ll hit you.\n");
        }

    }

    return 0;
}