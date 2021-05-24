#include <stdio.h>

int main()
{
   int T, R1, R2, i;

   scanf("%d", &T);
   
   for (i = 1; i <= T; i++)
   {
      scanf("%d%d", &R1, &R2);
      printf("%d\n", R1+R2);   

   }
   
   return 0;
}