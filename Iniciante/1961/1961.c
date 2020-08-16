#include <stdio.h>

int main(){
    int alturaPulo, nroCanos, i;
    int diffAlturas, ehGameOver = 0;

    scanf("%d %d", &alturaPulo, &nroCanos);
    
    int alturaCanos[nroCanos];
    
    for (i=0; i<nroCanos; i++){
        scanf("%d", &alturaCanos[i]);
    }
    
    for (i=0; i<nroCanos-1; i++){
        diffAlturas = abs(alturaCanos[i] - alturaCanos[i+1]);
        
        if (diffAlturas > alturaPulo){
            ehGameOver = 1;
            break;
        }    
    }

    if(ehGameOver == 0)
        printf("YOU WIN\n");
    else
        printf("GAME OVER\n");
    
    return 0;
}