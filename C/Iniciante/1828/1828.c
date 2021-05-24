#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main() {
	int T;
	scanf("%d",&T);
	
	int i;
	for(i=1; i<=T; i++){
		char *sheldon = (char*) malloc(sizeof(char));
		char *raj = (char*) malloc(sizeof(char));
		
		scanf("%s",sheldon);
		scanf("%s",raj);
		
		if(strcmp(sheldon, raj) == 0)
			printf("Caso #%d: De novo!\n",i);
			
		else{
			if(strcmp(sheldon, "pedra") == 0){
				if( (strcmp(raj, "tesoura") == 0) || (strcmp(raj, "lagarto") == 0) )
					printf("Caso #%d: Bazinga!\n",i);
				else
					printf("Caso #%d: Raj trapaceou!\n",i);
			}
			
			if(strcmp(sheldon, "tesoura") == 0){
				if( (strcmp(raj, "papel") == 0) || (strcmp(raj, "lagarto") == 0))
					printf("Caso #%d: Bazinga!\n",i);
				else
					printf("Caso #%d: Raj trapaceou!\n",i);
			}
			
			if(strcmp(sheldon, "lagarto") == 0){
				if( (strcmp(raj, "papel") == 0) || (strcmp(raj, "Spock") == 0))
					printf("Caso #%d: Bazinga!\n",i);
				else
					printf("Caso #%d: Raj trapaceou!\n",i);
			}
			
			if(strcmp(sheldon, "Spock") == 0){
				if( (strcmp(raj, "tesoura") == 0) || (strcmp(raj, "pedra") == 0))
					printf("Caso #%d: Bazinga!\n",i);
				else
					printf("Caso #%d: Raj trapaceou!\n",i);
			}
			
			if(strcmp(sheldon, "papel") == 0){
				if( (strcmp(raj, "pedra") == 0) || (strcmp(raj, "Spock") == 0))
					printf("Caso #%d: Bazinga!\n",i);
				else
					printf("Caso #%d: Raj trapaceou!\n",i);
			}
			
		}

	}
	
	
	return 0;
}
