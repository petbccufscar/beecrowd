#include <stdio.h>
#include <string.h>

int main () {
    int casos_testes, pessoas_grupo, idioma_igual, i, j;
    char idioma_atual[20], idioma_anterior[20];

    scanf("%d", &casos_testes);
    for (i=0; i<casos_testes; i++) {
        scanf("%d", &pessoas_grupo);
        scanf("%s", &idioma_anterior);
        idioma_igual = 1;
        for (j=0; j<(pessoas_grupo-1); j++) {
            scanf("%s", &idioma_atual);
            if (strcmp(idioma_anterior, idioma_atual)) {
                idioma_igual = 0;
            }
            else {
                strcpy(idioma_anterior, idioma_atual);
            }
        }
        if (idioma_igual) {
            printf("%s\n", idioma_atual);
        }
        else {
            printf("ingles\n");
        }
    }

    return 0;
}