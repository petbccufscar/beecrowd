#include <stdio.h>

int main()
{
    int p, j1, j2, r, a, vencedor, soma;

    scanf("%d %d %d %d %d", &p, &j1, &j2, &r, &a);
    soma = j1 + j2;

    if((soma%2==0 && p==1) || (soma%2==1 && p==0)) 
      vencedor = 1;
    else 
      vencedor = 2;
    if((r==1 && a==0) || (r==0 && a==1)) 
      vencedor = 1;
    else if(r==1 && a==1) 
      vencedor=2;

    printf("Jogador %d ganha!\n", vencedor);

    return 0;
}


   
