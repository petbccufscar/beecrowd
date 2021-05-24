#include <stdio.h>
#include <string.h>
#include <stdbool.h>

int contem_assinatura(char *, char *);

int main(){
	int instancia=1;
	bool i=true;
	char a[10], b[300001];
	
	while(i){		
		scanf("%s", a);

		if(strcmp(a, "0") != 0){
			if(instancia != 1)
			printf("\n");

			scanf("%s", b);
			printf("Instancia %d\n", instancia++);
			if(contem_assinatura(a, b)){
				printf("verdadeira\n");
			}
			else
				printf("falsa\n");
		} else{
			i=false;
		}
	}
	return 0;
}

int contem_assinatura(char *a, char *b){
    if(strstr(b, a))
        return 1;
    return 0;
}