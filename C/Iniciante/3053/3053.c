#include <stdio.h>

int main (){

	int N;
	char moeda;

	char copos[3], aux;
	int movimento, i;

	scanf("%d", &N);
	scanf("%s", &moeda);

	if(moeda == 'A')
		copos[0] = 'A';
			
	else if( moeda == 'B')
		copos[1] = 'B';
			
	else if( moeda == 'C')
		copos[2] = 'C';
	

	for(i = 0; i < N; i++){
		scanf("%d", &movimento);
		
		if( movimento == 1){

			aux = copos[0];
			copos[0] = copos[1];
			copos[1] = aux; 

		}else if(movimento == 2){
		    
		    aux = copos[1];
			copos[1] = copos[2];
			copos[2] = aux;
			
		}else if(movimento == 3){

			aux = copos[0];
			copos[0] = copos[2];
			copos[2] = aux;
		}

	}

	for(i = 0; i < 3; i++)
	    if(copos[i] == 'A' || copos[i] == 'B' || copos[i] == 'C')
	        printf("%c\n", i + 65);
	

return 0;
}