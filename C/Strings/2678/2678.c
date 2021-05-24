#include <stdio.h>
#include <stdlib.h>

int main() {
	char c;
	char *teclado = "22233344455566677778889999";

	while (scanf("%c", &c) != EOF) {
		if ('a' <= c && c <= 'z')
			printf("%c", teclado[c-'a']);
		if ('A' <= c && c <= 'Z')
			printf("%c", teclado[c-'A']);
		if ('0' <= c && c <= '9')
			printf("%c", c);
		if (c == '\n' || c == '*' || c == '#')
			printf("%c", c);
	}

	printf("\n");
	
	return 0;
}