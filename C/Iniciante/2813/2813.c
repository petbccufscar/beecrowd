#include <stdio.h>
#include <stdlib.h>
#include <string.h>
 
int main() {
 
    int n, i;
    char *ida = (char*) malloc(sizeof(char));
    char *volta = (char*) malloc(sizeof(char));
    
    int cCompra = 0;
    int cSobra = 0;
    int eCompra = 0;
    int eSobra = 0;
    
    scanf("%d",&n);
    
    for (i=0;i<n;i++){
        scanf("%s",ida);
        scanf("%s",volta);
   
        if(strcmp(ida, "chuva") == 0 && cSobra == 0){
            cCompra++;
            eSobra++;
        }
        else if(strcmp(ida, "chuva") == 0 && cSobra > 0){
            cSobra--;
            eSobra++;
            
        }
        
        if(strcmp(volta, "chuva") == 0 && eSobra == 0){
            cSobra++;
            eCompra++;
            
        }
        else if(strcmp(volta, "chuva") == 0 && eSobra > 0){
            cSobra++;
            eSobra--;
            
        }
    }
    printf("%d %d\n",cCompra, eCompra);
    
    return 0;
}