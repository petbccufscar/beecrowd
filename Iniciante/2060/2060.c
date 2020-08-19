#include <stdio.h>

int main()
{
   int N, i, L;
   int mult2 = 0, mult3 = 0, mult4 = 0, mult5 = 0;

   scanf("%d", &N);
   
   for (i = 0; i < N; i++)
   {
      scanf("%d", &L);
      if(L%2==0){
         mult2++;
      }
      if(L%3==0){
         mult3++;
      }
      if(L%4==0){
         mult4++;
      }
      if(L%5==0){
         mult5++;
      }   
   }
   printf("%d Multiplo(s) de 2\n", mult2);
   printf("%d Multiplo(s) de 3\n", mult3);
   printf("%d Multiplo(s) de 4\n", mult4);
   printf("%d Multiplo(s) de 5\n", mult5);

   return 0;
}
