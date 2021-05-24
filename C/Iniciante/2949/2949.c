#include <stdio.h>


int main(){
    char nome[100];
    char raca;
    int pessoas, i;
    int hobbits=0,magos=0,humanos=0,elfos=0,anoes=0;
    scanf("%d",&pessoas);
    for(i = 0; i < pessoas; i++){
        scanf("%s",&nome);
        scanf(" %c",&raca);
        switch(raca){
            case 'A':   
                anoes++;    
                break;
            case 'E':   
                elfos++;
                break;
            case 'H':   
                humanos++;  
                break;
            case 'M':   
                magos++;    
                break;
            case 'X':
                hobbits++;
                break;
        }
    }

    printf("%d Hobbit(s)\n%d Humano(s)\n%d Elfo(s)\n%d Anao(s)\n%d Mago(s)\n",hobbits,humanos,elfos,anoes,magos);
    return 0;
}