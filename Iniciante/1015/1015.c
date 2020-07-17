#include <stdio.h>
#include <math.h>

int main() 
{
   float x1, y1, x2, y2, distX, distY, dist;

   scanf("%f %f", &x1, &y1);

   scanf("%f %f", &x2, &y2);

   distX = x2-x1;

   distY = y2-y1;

   dist = sqrt(pow(distX,2)+pow(distY,2));

   printf("%.4f\n", dist);

   return (0);
}
