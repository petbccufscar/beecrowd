#include <stdio.h>
#include <string.h>

char resistente(char *, char *);

int main(){

	char a[101], b[101];
	
	while(scanf("%s", a) != EOF){
		scanf("%s", b);
		if(resistente(a, b))
			printf("Resistente\n");
		else
			printf("Nao resistente\n");
	}
	
	return 0;
}

char resistente(char *a, char *b){
	char *contem;

    contem = strstr(a, b);

    if(contem)
        return 1;
    return 0;
}