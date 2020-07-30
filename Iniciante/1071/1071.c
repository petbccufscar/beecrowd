#include <stdio.h>

int main() {
  int contador, X, Y, aux, soma;
  scanf("%d%d",&X,&Y);
  
  if(X>Y){
    aux=X;
    X=Y;
    Y=aux;
  }

  soma=0;
  for(contador=X+1; contador<Y; contador++){
    if(contador%2!=0)
      soma+=contador;
  }
    
  printf("%d\n",soma);
  return 0;
}