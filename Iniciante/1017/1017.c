#include <stdio.h>

int main() 
{
   int tempo, velocidade;
   float dist;

   scanf("%d", &tempo);

   scanf("%d", &velocidade);

   dist = tempo*velocidade;

   printf("%.3f \n", dist/12);

   return (0);
}
