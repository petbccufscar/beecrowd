#include <stdio.h>


int main()
{
   int cafe[3]; 
   int A1, A2, A3, i, menor;

   scanf("%d %d %d", &A1, &A2, &A3);

   cafe[0] = A2*2 + A3*4;
   cafe[1] = A1*2 + A3*2;
   cafe[2] = A1*4 + A2*2;

   menor = cafe[0];

   for (i = 1; i < 3; i++)
   {
      if(menor>cafe[i]){
         menor=cafe[i];
      }
   }
   printf("%d\n", menor);

   return 0;
}
