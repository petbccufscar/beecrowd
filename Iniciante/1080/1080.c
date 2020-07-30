#include <stdio.h>

int main() {
  int entrada[100];
  int maiorValor, posicao=0;
  int i;

  for(i=0; i<100; i++){
    scanf("%d",&entrada[i]);
    if(entrada[i] > entrada[posicao]){
      maiorValor = entrada[i];
      posicao = i;
    }
    else{
      maiorValor = entrada[posicao];
    }
  }

  printf("%d\n",maiorValor);
  printf("%d\n",posicao+1);

  return 0;

}
