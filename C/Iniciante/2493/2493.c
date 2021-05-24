#include <stdio.h>
#include <stdlib.h>

char nomeJogador[50][50];

int compara(const void *a, const void *b)
{
    const int *p1 = (const int *) a;
    const int *p2 = (const int *) b;

    return strcmp(nomeJogador[*p1], nomeJogador[*p2]);
}

int main(){

	int quantJogadores, x[50], y[50], z[50], expressao[50], naoProsseguira[50], flag, i;
	char resposta[50];

	while(scanf("%d", &quantJogadores) != EOF){

		flag = 0;

		for(i=0; i<quantJogadores; i++)
			scanf("%d %d=%d", &x[i], &y[i], &z[i]);

		for(i = 0; i < quantJogadores; i++)
			scanf("%s %d %c", &nomeJogador[i], &expressao[i], &resposta[i]);

		for (i = 0; i < quantJogadores; i++)
		{
			switch(resposta[i]){
				case '+':
					if(x[expressao[i]-1] + y[expressao[i]-1] != z[expressao[i]-1])
						naoProsseguira[flag++] = i;
					break;

				case '-':
					if(x[expressao[i]-1] - y[expressao[i]-1] != z[expressao[i]-1])
						naoProsseguira[flag++] = i;
					break;

				case '*':
					if(x[expressao[i]-1] * y[expressao[i]-1] != z[expressao[i]-1])
						naoProsseguira[flag++] = i;
					break;

				case 'I':
					if(x[expressao[i]-1] + y[expressao[i]-1] == z[expressao[i]-1] ||
					   x[expressao[i]-1] - y[expressao[i]-1] == z[expressao[i]-1] ||
					   x[expressao[i]-1] * y[expressao[i]-1] == z[expressao[i]-1])
						naoProsseguira[flag++] = i;
					break;
				}
		}

		if(flag == 0)
		 printf("You Shall All Pass!\n");

		else if (flag == quantJogadores)
			 printf("None Shall Pass!\n");

		else{
			qsort(naoProsseguira, flag, sizeof(int), compara);
		
			for(i = 0; i < flag -1; i++)
				printf("%s ", nomeJogador[naoProsseguira[i]]);

			printf("%s\n", nomeJogador[naoProsseguira[i]] );
		}
	}
	
	return 0;
}