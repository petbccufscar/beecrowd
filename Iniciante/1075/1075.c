#include <stdio.h>

int main()
{

    int cont, N;

    scanf("%d", &N);

    for(cont=1; cont<=10000; cont++){
		if(cont%N == 2){
        	printf("%d\n", cont);
        }
    }

return 0;
}