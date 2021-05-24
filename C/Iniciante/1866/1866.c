#include <stdio.h>

int main() {
	int C, N, contagem = 0;

	scanf("%d", &C);

	while (contagem < C) {
		scanf("%d", &N);

		if (N % 2 == 0) printf("0\n");
		else printf("1\n");

		contagem++;
	}

	return 0;
}