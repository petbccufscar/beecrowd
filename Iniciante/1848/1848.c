#include<stdio.h>

int main()
{
	char entrada[10];
	int grito = 3, piscada = 0;

	
	while(grito){
		fgets(entrada, sizeof(entrada), stdin);

		if(entrada[0]=='c'){
			printf("%d\n", piscada);
			piscada = 0;
			grito--;
		}
		else{
		    if(entrada[0] == '*')
				piscada += 4;
			if(entrada[1] == '*')
				piscada += 2;
			if(entrada[2] == '*')
				piscada += 1;
		}

	} 
	return 0;
}