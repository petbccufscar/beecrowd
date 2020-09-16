#include <stdio.h>
#include <math.h>

int main(){
  double ano;

  while (~scanf("%lf", &ano)){
    printf("%.lf\n", ceil(ano / 100.0));
  }

  return 0;
}