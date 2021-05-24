#include <stdio.h>

int main() {
  int quantidade_ra, i, j, k;
  char ra_enviados[100] = {'0'}, senha_provisoria[20] = {'0'};
  scanf("%d", &quantidade_ra);
  for(i = 0; i < quantidade_ra; i++) {
    scanf("%s", &ra_enviados);
    if(ra_enviados[0] == 'R' && ra_enviados[1] == 'A') {
      j = 2;
      while (ra_enviados[j] == '0') {
        j++;
      }
      k = 0;
      while (ra_enviados[j] != '\0') {
        senha_provisoria[k] = ra_enviados[j];
        k++;
        j++;
      }
      if(j==20) {
        printf("%s\n", senha_provisoria);
      }
    }
    else {
      printf("INVALID DATA\n");
    }
  }
  return 0;
}