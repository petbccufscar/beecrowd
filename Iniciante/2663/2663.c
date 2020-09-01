#include <stdio.h>

int main()
{
   int N, i, j, pivo, minclassificados;
   scanf("%d", &N);
   int Participantes[N];
   
   int numpassou;
   scanf("%d", &numpassou);



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

   j=numpassou;
   i=numpassou - 1;

   minclassificados=numpassou;

   while (Participantes[j++] == Participantes[i])
   {
         minclassificados++;                                         
   }
   
   printf("%d\n", minclassificados);

   return 0;
}