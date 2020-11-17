#include <stdio.h>
#include <string.h>

int main () {
    char rastro_processamento[50];
    int processos, i, ciclos_maquina, tam_rastro, sequencia_leituras;
    while(scanf("%s", &rastro_processamento) != EOF) {
        scanf("%d", &processos);
        tam_rastro = strlen(rastro_processamento);
        ciclos_maquina = 0;
        for (i=0; i <= tam_rastro; i++) {
            if (rastro_processamento[i] == 'R') {
                ciclos_maquina++;
                sequencia_leituras = 1;
                i++;
                while (rastro_processamento[i] == 'R') {
                    sequencia_leituras++;
                    i++;
                }
                while (sequencia_leituras > processos) {
                    ciclos_maquina++;
                    sequencia_leituras = sequencia_leituras - processos;
                }   
            }
            if (rastro_processamento[i] == 'W') {
                ciclos_maquina ++;
            }
        }
        printf("%d\n", ciclos_maquina);
    }
    return 0;
}