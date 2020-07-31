#include <stdio.h>

int main()
{
   int N[1000];
   int T, i, aux;
   scanf("%d", &T);
   aux = 0;
   for (i = 0; i < 1000; i++)
   {
      printf("N[%d] = %d\n", i, aux);
      aux++;
      if(aux==T){
         aux=0;
      } 
   }
   return 0;
}