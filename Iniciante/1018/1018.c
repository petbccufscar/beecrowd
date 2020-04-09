#include <stdio.h>
 
int main() {
 
int valor, c100, c50, c20, c10, c5, c2, c1;
 
 scanf ("%d", &valor);
 
 c100 = valor/100;
 c50 = (valor - c100*100)/50; 
 c20 = (valor - c100*100 - c50*50)/20;
 c10 = (valor - c100*100 - c50*50 - c20*20)/10;
 c5 = (valor - c100*100 - c50*50 - c20*20 - c10*10)/5;
 c2 = (valor - c100*100 - c50*50 - c20*20 - c10*10 - c5*5)/2;
 c1 = (valor - c100*100 - c50*50 - c20*20 - c10*10 - c5*5 - c2*2);
 
printf ("%d\n", valor);
printf ("%d nota(s) de R$ 100,00\n", c100);
printf ("%d nota(s) de R$ 50,00\n", c50);
printf ("%d nota(s) de R$ 20,00\n", c20);
printf ("%d nota(s) de R$ 10,00\n", c10);
printf ("%d nota(s) de R$ 5,00\n", c5);
printf ("%d nota(s) de R$ 2,00\n", c2);
printf ("%d nota(s) de R$ 1,00\n", c1);


return 0;

}