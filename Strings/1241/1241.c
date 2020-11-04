#include <stdio.h>
#include <string.h>


int main () {
    int casos_testes, a_tamanho, b_tamanho, encaixa, j, i;
    char a_valor[1000], b_valor[1000];

    scanf("%d", &casos_testes);
    for (i=0; i<casos_testes; i++) {
        scanf("%s", &a_valor);
        scanf("%s", &b_valor);

        a_tamanho = strlen(a_valor);
        b_tamanho = strlen(b_valor);

        encaixa = 0;
        for (j=1; j<=b_tamanho; j++) {
            if (a_valor[(a_tamanho-j)] == b_valor[(b_tamanho-j)]) {
                encaixa++;
            }
        }

        if (encaixa == b_tamanho) {
            printf("encaixa\n");
        }
        else {
            printf("nao encaixa\n");
        }
        
    }

    return 0;
}