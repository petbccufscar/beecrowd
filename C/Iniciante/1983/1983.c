#include <stdio.h>

int main() {
    int N, i, matricula, matriculaMaior;
    float nota, notaMaior;

    scanf("%d",&N);

    scanf("%d %f", &matriculaMaior, &notaMaior);

    for (i = 1; i < N; i++) {
        scanf("%d %f", &matricula, &nota);

        if (nota > notaMaior) {
            matriculaMaior = matricula;
            notaMaior = nota;
        }
    }

    if (notaMaior >= 8) {
        printf("%d\n", matriculaMaior);
    }

    else {
        printf("Minimum note not reached\n");
    }

    return 0;
}