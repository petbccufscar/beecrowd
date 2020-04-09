#include <stdio.h>
 
int main() {
 
int duracao, h, m, s;

scanf ("%d", &duracao);
 
h = duracao/3600;
m = (duracao - h*3600)/60;
s = duracao - h*3600 - m*60;

printf ("%d:%d:%d\n", h, m, s);

return 0;

}