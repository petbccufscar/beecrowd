#include <stdio.h>

int main()
{
   int N, i, j, pivo, classificados;
   scanf("%d", &N);
   int Participantes[N];
   
   int NumPassou;
   scanf("%d", &NumPassou);
   int Passou[NumPassou], cont=0;


   for (i = 0; i < N; i++)
   {
      scanf("%d", &Participantes[i]);
   }
   

   i = 1;
   while (i < N)
	{

		j = i - 1;
		pivo = Participantes[i];

		while (j >= 0 && Participantes[j] < pivo)
		{

			Participantes[j + 1] = Participantes[j];
			j--;

		}

		Participantes[j + 1] = pivo;
		i++;

	}

   j=NumPassou;
   i=NumPassou - 1;

   classificados=NumPassou;

   while (Participantes[j++] == Participantes[i])
   {
         classificados++;                                         
   }
   
   printf("%d\n", classificados);

   return 0;
}