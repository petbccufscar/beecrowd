#include <stdio.h>
#include <string.h>

int main(){
  int i;
  char texto[300];

  while (~scanf("%[^\n]%*c", texto)){
    for (i = 0; i < strlen(texto); i++){
      if (texto[i] == '@')
        texto[i] = 'a';
      else if (texto[i] == '&')
        texto[i] = 'e';
      else if (texto[i] == '!')
        texto[i] = 'i';
      else if (texto[i] == '*')
        texto[i] = 'o';
      else if (texto[i] == '#')
        texto[i] = 'u';        
    }

    for (i = 0; i < strlen(texto); i++){
      printf("%c", texto[i]);
    }

    printf("\n");
  }

  return 0;
}