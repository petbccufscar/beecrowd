#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(){
    int nroArabico;
    int indiceCentena, indiceDezena, indiceUnidade;
    
    char *unidades[11] = {"","I","II","III","IV","V","VI","VII","VIII","IX","\0"};
    char *dezenas[11] = {"","X","XX","XXX","XL","L","LX","LXX","LXXX","XC","\0"};
    char *centenas[11] = {"","C","CC","CCC","CD","D","DC","DCC","DCCC","CM","\0"};
    char *nroRomano;
    nroRomano = (char*)malloc(12*sizeof(char));
    
    scanf("%d", &nroArabico);
  
    indiceCentena = nroArabico/100;
    indiceDezena = (nroArabico%100)/10;
    indiceUnidade = nroArabico%10;
    
    strcat(nroRomano, centenas[indiceCentena]);
    strcat(nroRomano, dezenas[indiceDezena]);
    strcat(nroRomano, unidades[indiceUnidade]);
    
    printf("%s\n", nroRomano);
    
    return 0;
}