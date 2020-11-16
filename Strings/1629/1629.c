#include <stdio.h>
#include <string.h>

int somaDigitos(int n);

int main()
{
	char s[1000];
    	int tamanho, casos;
	
	while (1)
	{
		scanf("%d", &casos);
		if (casos == 0) return 0;
		while (casos--)
		{
			scanf("%s", s);
            		tamanho = strlen(s);
		
			int uns = 0;
			int zeros = 0;
			for (i = 0; i < tamanho; i += 2)
				zeros += (s[i] - '0');
			for (int i = 1 ; i < tamanho; i += 2)
				uns += (s[i] - '0');
		
			zeros = somaDigitos(zeros);
			uns = somaDigitos(uns);
		
			printf("%d\n", zeros + uns);
		}
	}
}

int somaDigitos(int n)
{
	int soma = 0;
	
	while (n > 0)
	{
		soma += (n % 10);
		n /= 10;
	}
	return soma;
}
