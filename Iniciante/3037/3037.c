#include <stdio.h>

int main(){

    int n, jogadas, distanciaCentro, distanciaJogador;
    int pontos[2];

    scanf("%d", &n);

    while (n--){

        jogadas = 6;
        pontos[0] = 0;
        pontos[1] = 0;

        while (jogadas>3){

            scanf("%d %d", &distanciaCentro, &distanciaJogador);
            pontos[0] += distanciaCentro * distanciaJogador;
            jogadas --;
        }

        while (jogadas--){
            
            scanf("%d %d", &distanciaCentro, &distanciaJogador);
            pontos[1] += distanciaCentro * distanciaJogador;
        }

        if(pontos[0] > pontos[1])
            printf("JOAO\n");

        else
            printf("MARIA\n");
    }
    
    return 0;
}