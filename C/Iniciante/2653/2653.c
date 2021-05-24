#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct no{
    char joia[1000000];
    struct no *esq;
    struct no *dir;

} no;

int numJoias = 0;

no * adiciona(no *ramo, char *p){
    if (!ramo){
        ramo = (no * ) malloc(sizeof(no));
        ramo->esq = ramo->dir = NULL;
        strcpy(ramo->joia, p);
        numJoias++;

    }
    else if (strcmp(ramo->joia, p) > 0)
        ramo->esq = adiciona(ramo->esq, p);
    else if (strcmp(ramo->joia, p) < 0)
        ramo->dir = adiciona(ramo->dir, p);

    return ramo;
}

int main(int argc, char **argv){
    char novaJoia[1000000];

    no *arvore = NULL;

    while (scanf("%s", joia) != EOF)
        arvore = adiciona(arvore, novaJoia);

    printf("%d\n", numJoias);

    return 0;

}
