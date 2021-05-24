#include <stdio.h>

int main() {
	int saida, voo, fuso, chegada;

  scanf("%d %d %d", &saida, &voo, &fuso);

  if(saida == 0)
  	saida = 24;

  chegada = ((saida + voo + fuso) % 24);

  printf("%d\n", chegada);

	return 0;
}