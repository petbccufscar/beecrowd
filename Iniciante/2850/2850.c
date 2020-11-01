#include <stdio.h>
#include <string.h>
 
int main() {
    char condicao[15];
    
    while (scanf(" %15[^\n]", condicao) != EOF) {
        if (!strcmp(condicao, "esquerda"))
            printf("ingles\n");
        else if (!strcmp(condicao, "direita"))
            printf("frances\n");
        else if (!strcmp(condicao, "nenhuma"))
            printf("portugues\n");
        else if (!strcmp(condicao, "as duas"))
            printf("caiu\n");
    }
 
    return 0;
}
