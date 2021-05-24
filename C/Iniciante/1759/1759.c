#include <stdio.h>

int main()
{
   int N, i;

   scanf("%d", &N);
   
   for (i = 1; i <= N; i++)
   {
      if(i==N)
         printf("Ho!\n");
      else
         printf("Ho ");
       
   }
   
   return 0;
}