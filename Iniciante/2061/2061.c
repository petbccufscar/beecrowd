#include <stdio.h>
#include <string.h>

int main()
{
   int N, i, M;
   char str[20];
   
   scanf("%d %d", &N, &M);
   
   for (i = 0; i < M; i++)
   {
      scanf("%s", str);
      
      if(strcmp(str, "fechou")==0){
         N++;
      }
      else if(strcmp(str, "clicou")==0){
         N--;
      }
    
   }
   printf("%d\n", N);
   return 0;
}
