#include <stdio.h>

int main() {
  int N;
  int i;
  int numero = 1 ;
  scanf("%d",&N);

  for(i = 1; i <= N; i++)	{
    printf("%d %d %d PUM\n", numero, numero + 1, numero + 2);
    numero = numero + 4;
  }

  return 0;

}
