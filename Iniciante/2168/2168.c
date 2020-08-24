#include <stdio.h>


int main()
{
   int N;
   scanf("%d", &N);
   int M[N+1][N+1];
   int i, j;

   for (i = 0; i <= N; i++)
   {  
      for (j = 0; j <= N; j++)
      {
         scanf("%d", &M[i][j]);
      } 
   }
   
   for (i = 0; i < N; i++)
   {  
      for (j = 0; j < N; j++)
      {
         if(M[i][j]+M[i][j+1]+M[i+1][j]+M[i+1][j+1] < 2)
            printf("U");
         else 
            printf("S");
      }
      printf("\n");
   }


   return 0;
}
