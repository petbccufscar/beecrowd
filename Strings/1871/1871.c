#include <stdio.h>

int main() {
  
  int m, n, soma, i, posi;
  char num[21];

  while(1){
    scanf("%d %d", &m, &n);

    if(m == 0 && n == 0){
      break;
    }

    soma = m + n;
    posi = sprintf(num, "%d", soma);

    num[posi + 1] = '\0';

    for(i = 0; i < posi; i++) {
      if(num[i] != '0') {
        printf("%c", num[i]);
      }
    }
    printf("\n");
  }

  return 0;
}