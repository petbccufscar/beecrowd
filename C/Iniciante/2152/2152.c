#include <stdio.h>

int main(){
    int numTestes, hora, minuto, abriu;
     
    scanf("%d", &numTestes);

    while(numTestes){

     	scanf("%d %d %d", &hora, &minuto, &abriu);
        printf("%02d:%02d - A porta ", hora, minuto);
       
        if(abriu)
            printf("abriu!\n");
        else
            printf("fechou!\n");

        numTestes--;
    }

	return 0;
}