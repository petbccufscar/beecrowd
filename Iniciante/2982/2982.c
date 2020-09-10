#include <stdio.h>

int main(){
  char op;
  int i, n, valor, total = 0;
  scanf("%d%*c", &n);

  for (i = 0; i < n; ++i){
    scanf("%c %d%*c", &op, &valor);

    if (op == 'G')
			total -= valor;
    else
      total += valor;
	}

  if (total >= 0)
  	printf("A greve vai parar.\n");
  else
  	printf("NAO VAI TER CORTE, VAI TER LUTA!\n");

  return 0;

}