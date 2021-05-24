#include <stdio.h>

 int main(){
   char caractere;
   int encontrado_negrito, encontrado_italico;

   encontrado_negrito = 0;
   encontrado_italico = 0;

   while(scanf("%c", &caractere) != EOF){
     if(caractere == '*'){
       if(encontrado_negrito == 0){
         printf("<b>");
         encontrado_negrito = 1;
       }
       else if(encontrado_negrito == 1){
         printf("</b>");
         encontrado_negrito = 0;
       }
     }
     else if(caractere == '_'){
       if(encontrado_italico == 0){
         printf("<i>");
         encontrado_italico = 1;
       }
       else if(encontrado_italico == 1){
         printf("</i>");
         encontrado_italico = 0;
       }
     }
     else{
       printf("%c", caractere);
     }
   }

   return 0;
 }
