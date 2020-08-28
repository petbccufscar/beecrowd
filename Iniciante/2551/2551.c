#include <stdio.h>

int main () {
  int N, recorde_D, recorde_T, i, T, D;
  
  while (scanf("%d", &N) != EOF) {
  
  recorde_D = 0; 
  recorde_T = 1;

    for (i = 1; i <= N; i++) {
      scanf("%d %d", &T, &D);

      if (D*recorde_T > recorde_D*T) {
        printf("%d\n", i);
        recorde_D = D;
        recorde_T = T;
      }
    }
  }
  return 0;
}