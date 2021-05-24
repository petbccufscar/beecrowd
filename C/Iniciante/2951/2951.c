#include <stdio.h>

int main () {
    char runa_atual, letras_runas[100];
    int runas_existentes, amizade_necessaria, valor_amizade = 0, runas_recitadas, j, i, valor_runas[100];
    
    scanf("%d", &runas_existentes);
    scanf("%d", &amizade_necessaria);


    for (i=0; i<runas_existentes; i++) {
        scanf(" %c %d", &letras_runas[i], &valor_runas[i]);
    }
    scanf(" %d", &runas_recitadas);

    for (i=0; i<runas_recitadas; i++) {
        scanf(" %c", &runa_atual);
        for (j=0; j<runas_existentes; j++) {
            if (runa_atual == letras_runas[j]) {
                valor_amizade += valor_runas[j];
            }
        }
    }
    printf("%d\n", valor_amizade);
    if (valor_amizade >= amizade_necessaria) {
        printf("You shall pass!\n");
    }
    else {
        printf("My precioooous\n");
    }
    return 0;
}