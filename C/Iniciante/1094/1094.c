#include <stdio.h>

int main() {
  int N=0, Quantia;
  int coelhos=0, ratos=0, sapos=0, total=0;
  int i;
  float percentual;
  char Tipo;

  scanf("%d",&N);

  for(i=0; i<N; i++){
    scanf("%d %c",&Quantia,&Tipo);

    if(Tipo == 'C'){
      coelhos = coelhos + Quantia;
    }

    if(Tipo == 'R'){
      ratos = ratos + Quantia;
    }

    if(Tipo == 'S'){
      sapos = sapos + Quantia;
    }
  }

  total = coelhos+ratos+sapos;

  printf("Total: %d cobaias\n",total);
  printf("Total de coelhos: %d\n",coelhos);
  printf("Total de ratos: %d\n",ratos);
  printf("Total de sapos: %d\n",sapos);

  percentual = (coelhos*100.00)/total;
  printf("Percentual de coelhos: %.2f %%\n",percentual);

  percentual = (ratos*100.00)/total;
  printf("Percentual de ratos: %.2f %%\n",percentual);
  
  percentual = (sapos*100.00)/total;
  printf("Percentual de sapos: %.2f %%\n",percentual);

  return 0;

}
