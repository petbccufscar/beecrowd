#include <stdio.h>

int main(){
  int v, p, i;
  scanf("%d %d", &v, &p);

  for (i = 1; i < 10; ++i){
   	printf("%d%c", (i*v*p)%10 ? ((i*v*p)/10)+1 : (i*v*p)/10, i<9 ? ' ' : '\n');
  }

  return 0;
}