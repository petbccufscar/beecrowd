#include <stdio.h>
 
int main() {
 
    int M, N[40], C[40], i;
    double resultado, cima, baixo;
 

    while(scanf("%d",&M) != EOF ) {


    for ( i=0; i<M; i++ ) {
        scanf("%d %d", &N[i], &C[i]);
    }
 
    resultado = 0;
    cima = 0;
    baixo = 0;
 
    for ( i=0; i<M; i++ ) {
        cima = cima + ( N[i]*C[i] ) ;
    }
 
    for ( i=0; i<M; i++ ) {
        baixo = baixo + ( C[i] * 100) ;
    }
 
    resultado = cima / baixo;
 
    printf("%.4lf\n",resultado);
 
 
    }


    return 0;
}