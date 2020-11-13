#include <stdio.h>
#include <string.h>

int main(){		
	
	char pomedex[151][1001], pomekon[1001];
	int i, n, topo, quant;

	topo = -1;
	quant = 1;	
	
	scanf("%d", &n);
	
	while(n--){
		
		scanf("%s", pomekon);
		
		if(topo == -1)
			strcpy(pomedex[++topo], pomekon);

		else{

			i=0;

			while(i <= topo && strcmp(pomedex[i],pomekon))
				i++;
			
			if(i>topo){
				strcpy(pomedex[++topo], pomekon);
				quant++;
		 	}
		}		
	}
	
	printf("Falta(m) %d pomekon(s).\n", 151 - quant);
	
	return 0;
}