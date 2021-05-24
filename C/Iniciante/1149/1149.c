#include <stdio.h>
int main() {

    int A, N, i, soma;

    soma = 0;

    scanf("%d %d", &A, &N);

    while (N <= 0) {
        scanf("%d", &N);
    }
    
    for (i = 0; i < N; i++) {
        soma += (A + i);
    }

    printf("%d\n", soma);

    return 0;
}