#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(){
	int V;
	scanf("%d",&V);
	
	char digitosHexa[17] = {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F'};
	char *Vhexa = (char*) malloc(sizeof(char));
	int i = 0;

	while(V > 0){
		Vhexa[i] = digitosHexa[V%16];
    		V = V/16;
    		i = i + 1;
	}
   
	i = i - 1;
    
	for(i; i >= 0; i--){
		printf("%c", Vhexa[i]);
	}
	printf("\n");
	
	return 0;
}
