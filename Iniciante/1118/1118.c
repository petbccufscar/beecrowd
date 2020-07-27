#include <stdio.h>

int main() {

    double nota, media, nro_notas;
    int x;
    
    media = 0;
    nro_notas = 0;
    while(1) {
        scanf("%lf", &nota);
        if(nota < 0 || nota > 10)
            printf("nota invalida\n");
        else {
            media = media + nota;
            nro_notas++;
            if(nro_notas == 2) {
                media = media/2;
                printf("media = %0.2lf\n", media);
                printf("novo calculo (1-sim 2-nao)\n");
                
                while(1) {
                    scanf("%d",&x);
                    if(x == 1) {
                        media = 0;
                        nro_notas = 0;
                        break;
                    }
                    else if(x == 2)
                        return 0;
                    else
                        printf("novo calculo (1-sim 2-nao)\n");
                }
            }
        }
    }
    return 0;
}
