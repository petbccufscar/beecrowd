#include <stdlib.h>
#include <stdio.h>
#include <string.h>

#define TAM_MAX 102

int main(){
  char linha[TAM_MAX], nova_linha[TAM_MAX];
  int i, j, tam_linha, casos;

  scanf("%d", &casos);
  linha[0] = getchar();

  while(casos > 0){
    fgets(linha, TAM_MAX, stdin);
    tam_linha = strlen(linha);

    if(linha[tam_linha-1] == '\n'){
      linha[tam_linha-1] = '\0';
      tam_linha--;
    }

    for(i=tam_linha/2 - 1, j=0; i >= 0; i--, j++){
      nova_linha[j] = linha[i];
    }

    for(i=tam_linha-1; i > tam_linha/2 - 1; i--, j++){
      nova_linha[j] = linha[i];
    }

    nova_linha[j] = '\0';

    printf("%s\n", nova_linha);

    casos--;
  }
  return 0;
}
