#include <stdio.h>

int main(){
	int i;
	char palavra[40];

	for (i = 1; i <= 10; i++){
		scanf("%s", palavra);

		if (i == 3 || i == 7 || i == 9)
			printf("%s\n", palavra);
	}

	return 0;
}