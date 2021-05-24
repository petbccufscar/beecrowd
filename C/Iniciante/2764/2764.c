#include <stdio.h>

int main() {
  int dia, mes, ano;

	scanf("%d/%d/%d", &dia, &mes, &ano);

  printf("%02d/%02d/%02d\n", mes, dia, ano);
  printf("%02d/%02d/%02d\n", ano, mes, dia);
  printf("%02d-%02d-%02d\n", dia, mes, ano);

  return 0;
}