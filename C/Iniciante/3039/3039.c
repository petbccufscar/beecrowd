#include <stdio.h>
#include <stdlib.h>
 
int main() {
 
    int n, i, carrinho, boneca;
    char *nome = (char*) malloc(sizeof(char));
    char genero;

    carrinho = 0;
    boneca = 0;
    
    scanf ("%d",&n);
    
    for (i=0;i<n;i++){
        scanf ("%s ", nome);
        scanf ("%c", &genero);
        
        if (genero == 'F')
            boneca++;
        else
            carrinho++;
    }
    printf ("%d carrinhos\n", carrinho);
    printf ("%d bonecas\n", boneca);
    
    return 0;
}