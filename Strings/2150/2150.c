#include <stdio.h>
#include <string.h>

int main(){

	char vogais[40], texto[500];
	int contaVogais, i, j;

	while(scanf("%s ", vogais) != EOF){

		fgets(texto, sizeof(texto), stdin);

		contaVogais = 0;

		for(i=0;i<strlen(vogais); i++){
			for(j=0; j<strlen(texto); j++){
				if(vogais[i] == texto[j])
					contaVogais++;
			}
		}

		printf("%d\n", contaVogais);
	}

	return 0;
}
