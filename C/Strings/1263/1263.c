#include <stdio.h>
#include <string.h>
#include <ctype.h>

int main(){
    char frase[5099];
    int espaco, inicial, count, ehSequencia; 

    while(fgets(frase, sizeof(frase), stdin) != NULL){ 
        inicial = 0; 
        count = 0;
        ehSequencia = 0;

        for(espaco = 0; espaco < strlen(frase); espaco++)
            if (frase[espaco] == ' '){
                if(tolower(frase[inicial]) == tolower(frase[espaco+1])){
                    if(!ehSequencia){
                        count++;
                        ehSequencia = 1;
                    }
                }
                else
                    ehSequencia = 0;
                
                inicial = espaco+1;
            }

        printf("%d\n", count);        
    }

    return 0;
}