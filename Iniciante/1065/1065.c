#include <stdio.h>

int main() 
{
    int contPares = 0;
    int valor;

    int i ;  
    for( i = 0; i < 5; i++){
            scanf("%d", &valor);
            if( valor%2 == 0){
                contPares++;  
            }
    }

    printf("%d valores pares\n", contPares);

   return (0);
}