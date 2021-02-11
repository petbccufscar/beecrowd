#include <stdlib.h>
#include <stdio.h>
#include <string.h>

#define MAX_PALAVRA 102
int main(){

  int n, i, j, k, min_tam_i, min_tam, achou;
  char aux[MAX_PALAVRA];
  char *linha;
  char ** linhas;

  scanf("%d", &n);

  linhas = malloc(sizeof(char*)*n);

  min_tam = 1001;
  for(i=n-1; i >= 0; i--){
    linha = malloc(sizeof(char)*MAX_PALAVRA);
    scanf("%s", linha);
    linhas[i] = linha;
    if(strlen(linhas[i]) < min_tam){
      min_tam_i = i;
      min_tam = strlen(linhas[i]);
    }
  }

  achou = 0;

  for(i=min_tam; i > 0 && achou == 0; i--){
    for(k=0; k + i <= min_tam && achou == 0; k++){
      strncpy(aux, &linhas[min_tam_i][k], i);
      aux[i] = '\0';
      achou = 1;
      for(j=0; j < n && achou == 1; j++){
        if(strstr(linhas[j], aux) == NULL){
          achou = 0;
        }
      }
    }
  }

  printf("%s\n", aux);

  return 0;
}
