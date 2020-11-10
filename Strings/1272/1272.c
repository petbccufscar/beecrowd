#include <stdio.h>
#include <string.h>

int main(){
	int N, i, j;
	char texto[52], mensagemOculta[52];

	scanf("%d ", &N);

	while(N>0){

		fgets(texto, sizeof(texto), stdin);

		j = 0;
		
		for(i = 0; i < strlen(texto)-1; i++){

			if(texto[i] != ' ' && (texto[i-1] == ' ' || !i))
				mensagemOculta[j++] = texto[i]; 
		}

		mensagemOculta[j] = '\0';

		printf("%s\n", mensagemOculta);
		N--;
	}

	return 0;
}