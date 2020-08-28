#include <stdio.h>
#include <stdlib.h>

int main() {
	int N, i;	
	char *mensagem = (char*) malloc(sizeof(char));
	
	scanf("%d",&N);
	
	for(i=1; i<=N; i++){
		scanf("%s",mensagem);
		printf("I am Toorg!\n");
		fflush(stdin);
	}
	
	return 0;
}
