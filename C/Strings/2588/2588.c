#include <stdlib.h>
#include <stdio.h>
#define TAM_MAX 1002

void ordena_sequencia(char *sequencia){
 int i, j;
 char aux;
 for(i=0; sequencia[i+1] != '\n' && sequencia[i+1] != '\0'; i++){
   for(j=i+1; j-1 >= 0 && sequencia[j] <= sequencia[j-1]; j--){
     aux = sequencia[j];
     sequencia[j] = sequencia[j-1];
     sequencia[j-1] = aux;
   }
 }
}

int main(){
  char sequencia[TAM_MAX];
  int i, par, aux, caracteres_faltantes;
  while(scanf("%s", sequencia) != EOF){
    ordena_sequencia(sequencia);
    par = 0;
    caracteres_faltantes = 0;
    aux = sequencia[0];
    for(i=0; sequencia[i] != '\n' && sequencia[i] != '\0'; i++){
      if(sequencia[i] != aux){
        caracteres_faltantes += par;
        par = 0;
        aux = sequencia[i];
      }
      if(par == 1)
        par--;
      else if(par == 0)
        par++;
    }
    caracteres_faltantes += par;
    if(caracteres_faltantes != 0){
      printf("%d\n", caracteres_faltantes-1);
    }
    else{
      printf("%d\n", caracteres_faltantes);
    }
  }
  return 0;
}
