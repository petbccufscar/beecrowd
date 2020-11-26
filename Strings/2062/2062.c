#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define TAM_MAX 22

int main(){

  char palavra[TAM_MAX];
  int primeiro, num_palavras;

  scanf("%d", &num_palavras);
  primeiro = 1;

  while(num_palavras > 0){
    scanf("%s", palavra);

    if(primeiro == 0){
      printf(" ");
    }
    else{
      primeiro = 0;
    }

    if(strlen(palavra) == 3 && palavra[0] == 'O' && palavra[1] == 'B' && palavra[2] != 'I'){
      printf("OBI");
    }
    else if(strlen(palavra) == 3 && palavra[0] == 'U' && palavra[1] == 'R' && palavra[2] != 'I'){
      printf("URI");
    }
    else{
      printf("%s", palavra);
    }

    num_palavras--;
  }
  printf("\n");
  return 0;
}
