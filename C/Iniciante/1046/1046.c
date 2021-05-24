#include <stdio.h>
#include <math.h>

int main()
{
	int h_inicio, h_fim;
	scanf("%d%d", &h_inicio, &h_fim);
	if (h_inicio>12 && h_fim<12)
	{
		printf("O JOGO DUROU %d HORA(S)\n", abs(abs(h_inicio-12)-(h_fim+12)));
	}
	if (h_inicio==0&&h_fim==0 || h_inicio==h_fim)
	{
		printf("O JOGO DUROU 24 HORA(S)\n");
	}
	if (h_inicio<12&&h_fim>12)
	{
		printf("O JOGO DUROU %d HORA(S)\n", abs((h_inicio+12)-abs(h_fim+12)));
	}
	
}