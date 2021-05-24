#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct no{
    char email[100];
    struct no *esq;
    struct no *dir;

} no;

int emailsUnicos = 0;

void limpa(char *original){
    char aux[101];
    int i = 0, j = 0;    
    while (original[i]){
        
        if (original[i] == '+'){
            break;
        }
        else if(original[i] == '.'){
            i++;
        }
        else{
            aux[j] = original[i];
            j++;
            i++;
        }
    }
    
    for(i = 0; i < j; i++)
        original[i] = aux[i];

    original[i] = '*';
    
}

no * adiciona(no *ramo, char *nome){
    if (!ramo){
        ramo = (no * ) malloc(sizeof(no));
        ramo->esq = ramo->dir = NULL;
        strcpy(ramo->email, nome);
        emailsUnicos++;
    }
    else if (strcmp(ramo->email, nome) > 0)
        ramo->esq = adiciona(ramo->esq, nome);
    else if (strcmp(ramo->email, nome) < 0)
        ramo->dir = adiciona(ramo->dir, nome);

    return ramo;
}

int main(int argc, char **argv){
    int n;
    char usuario[100];
    char dominio[100];
    no *arvore = NULL;
    char* usuarioLimpo;
    scanf("%d", &n);

    while (n--){
        scanf(" %[^@]%s", usuario, dominio);
        limpa(usuario);
        usuarioLimpo = strtok(usuario, "*");
        strcat(usuarioLimpo, dominio);
        arvore = adiciona(arvore, usuarioLimpo);
    }

    printf("%d\n", emailsUnicos);

    return 0;

}
