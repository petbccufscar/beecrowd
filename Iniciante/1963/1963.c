#include <stdio.h>
#include <stdio.h>

int main(){
	double valorInicial, valorNovo;
     
    scanf("%lf %lf", &valorInicial, &valorNovo);
     
    printf("%.2lf%%\n", ( (valorNovo/valorInicial)-1)*100);

    return 0;
}