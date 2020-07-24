#include <stdio.h>

int main() {
  int entrada[100];
  int valor, posicao=0;
  int i;

  for(i=0; i<100; i++){
    scanf("%d",&entrada[i]);
    if(entrada[i] > entrada[posicao]){
      valor = entrada[i];
      posicao = i;
    }
    else{
      valor = entrada[posicao];
    }
  }

  printf("%d\n",valor);
  printf("%d\n",posicao+1);

  return 0;

}
