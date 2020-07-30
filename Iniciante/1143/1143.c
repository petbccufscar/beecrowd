#include <stdio.h>
#include <math.h>

int main() {
  int N;
  int i;
  int num1;
  int num2;
  scanf("%d",&N);

  for(i = 1; i <= N; i++)	{
    num1 = pow(i,2);
    num2 = pow(i,3);
    printf("%d %d %d\n", i, num1, num2);
  }
  return 0;

}
