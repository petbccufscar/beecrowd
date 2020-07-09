#include <stdio.h>

int main() 
{
    int contPares = 0;
    int contImpares = 0;
    int contPositivos = 0;
    int contNegativos = 0;
    int valor;

    int i ;
    for( i = 0; i < 5; i++){
            scanf("%d", &valor);
            if( valor%2 == 0){
                contPares++; 
                        if( valor > 0){
                                contPositivos++;
                        }else if( valor != 0){
                                contNegativos++;
                        }
            }else{
                        contImpares++;
                        if( valor > 0){
                                contPositivos++;
                        }else if( valor != 0){
                                contNegativos++;
                        }
                }
        }

    printf("%d valor(es) par(es)\n", contPares);
    printf("%d valor(es) impar(es)\n", contImpares);
    printf("%d valor(es) positivo(s)\n", contPositivos);
    printf("%d valor(es) negativo(s)\n", contNegativos);

   return (0);
}