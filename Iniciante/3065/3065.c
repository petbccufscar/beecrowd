#include <stdio.h>

int main() {
    int operando, expressao, i, teste = 0, resultado;
    scanf("%d", &operando);
    while (operando != 0) {
        resultado = 0;
        teste += 1;
        for (i=1; i<=operando; i++) {
            scanf("%d", &expressao);
            resultado += expressao;
        }
        printf("Teste %d\n", teste);
        printf("%d\n\n", resultado);
        scanf("%d", &operando);
    }
    return 0;
}