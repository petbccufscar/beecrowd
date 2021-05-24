#include <stdio.h>
#include <string.h>
 
int main() {

  char rajesh[15], sheldon[15];
  char pedra[] = "pedra", papel[] = "papel", tesoura[] = "tesoura", lagarto[] = "lagarto", spock[] = "spock";
  int c, i, comp;

  scanf("%d", &c);
  
  for(i = 0; i < c; i++) {
    
    scanf("%s %s", rajesh, sheldon);
    
    comp = strcmp(rajesh, sheldon);

    if (comp == 0) {
        printf("empate\n");
    } else if ((strcmp(rajesh, tesoura) == 0) && ((strcmp(sheldon, papel) == 0) || (strcmp(sheldon, lagarto) == 0))) {
        printf("rajesh\n");
    } else if ((strcmp(sheldon, tesoura) == 0) && ((strcmp(rajesh, papel) == 0) || (strcmp(rajesh, lagarto) == 0))) {
        printf("sheldon\n");
    } else if ((strcmp(rajesh, papel) == 0) && ((strcmp(sheldon, pedra) == 0) || (strcmp(sheldon, spock) == 0))) {
        printf("rajesh\n");
    } else if ((strcmp(sheldon, papel) == 0) && ((strcmp(rajesh, pedra) == 0) || (strcmp(rajesh, spock) == 0))) {
        printf("sheldon\n");
    } else if ((strcmp(rajesh, pedra) == 0) && ((strcmp(sheldon, lagarto) == 0) || (strcmp(sheldon, tesoura) == 0))) {
        printf("rajesh\n");
    } else if ((strcmp(sheldon, pedra) == 0) && ((strcmp(rajesh, lagarto) == 0) || (strcmp(rajesh, tesoura) == 0))) {
        printf("sheldon\n");
    } else if ((strcmp(rajesh, lagarto) == 0) && ((strcmp(sheldon, spock) == 0) || (strcmp(sheldon, papel) == 0))) {
        printf("rajesh\n");
    } else if ((strcmp(sheldon, lagarto) == 0) && ((strcmp(rajesh, spock) == 0) || (strcmp(rajesh, papel) == 0))) {
        printf("sheldon\n");
    } else if ((strcmp(rajesh, spock) == 0) && ((strcmp(sheldon, tesoura) == 0) || (strcmp(sheldon, pedra) == 0))) {
        printf("rajesh\n");
    } else if ((strcmp(sheldon, spock) == 0) && ((strcmp(rajesh, tesoura) == 0) || (strcmp(rajesh, pedra) == 0))) {
        printf("sheldon\n");
    }
    
}
    
    return 0;
}