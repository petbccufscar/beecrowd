#include<stdio.h>

int main(){

	int hora, minuto;

	while(scanf("%d:%d", &hora, &minuto)!=EOF){

		printf("Atraso maximo: ");

		if(hora<7 || (hora==7 && minuto==0))
			printf("0\n");
		else{
			minuto = ((hora + 1)-8)*60 + minuto;
			printf("%d\n", minuto);
		}
	}
	return 0;
}