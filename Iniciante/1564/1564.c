#include <stdio.h>

int main()
{
   int N;
   while ((scanf("%d", &N)!=EOF)&&(N<=100)&&(N>=0))
   {
      if(N==0){
         printf("vai ter copa!\n");
      }
      else
      {
         printf("vai ter duas!\n");
      }
      
   }
   
   return 0;
}