#include <stdio.h>
#include <string.h>

void faz_linha(){
    int i;
    for(i=0;i<39;i++)
        printf("-");
    printf("\n");
}

int main(){
    int decimais[16] = {0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15};
    int octais[16] = {0,1,2,3,4,5,6,7,10,11,12,13,14,15,16,17};
    int i=0, k=0;

    faz_linha();

    for(i=0;i<39;i++) {
        if((i==0) || (i==12) || (i==22) || (i==38)) {
            printf("|");
        }
        else if(i==3) {
            printf("decimal");
            i += strlen("decimal") - 1;
        }

        else if(i==15) {
            printf("octal");
            i += strlen("octal") - 1;
        }

        else if(i==25) {
            printf("Hexadecimal");
            i += strlen("Hexadecimal") - 1;
        }
        else
            printf(" ");
    } 
    printf("\n");

    faz_linha();

    for(k=0;k<16;k++) {
        for(i=0;i<39;i++){
            if((i==0) || (i==12) || (i==22) || (i==38)) {
                printf("|");
            }
            else if((i==7)||((i==6) && (k > 9))){
                printf("%d",decimais[k]);
                if(k>9)
                    i++;    
            }

            else if((i==17) ||((i==16) && (k > 7))){
                printf("%d",octais[k]);
                if(k>7)
                    i++;
            }

            else if(i==30) {
                switch(k){
                    case 10 : printf ( "A" ); break; 		
				    case 11 : printf ( "B" ); break;
				    case 12 : printf ( "C" ); break;
				    case 13 : printf ( "D" ); break;
				    case 14 : printf ( "E" ); break;
				    case 15 : printf ( "F" ); break;
                    default:  printf("%d",decimais[k]);
                }
              
            }
            else
                printf(" ");
        }
        printf("\n");
    }

    faz_linha();

    return 0;
}