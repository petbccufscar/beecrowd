#include<stdio.h>

int main(){
	int cha, degustador, acertos, i;

	acertos = 0;

	scanf("%d", &cha);

	for(i=0; i<5; i++){
		scanf("%d", &degustador);

		if(cha == degustador)
			acertos++;
	}
	printf("%d\n", acertos);

	return 0;
}8min