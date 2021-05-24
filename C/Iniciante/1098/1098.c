#include <stdio.h>

int main(){
    double i = 0;
    int k, contador=0;

    while(i<2){
        for(k=1;k<=3;k++){
            
            if (contador%5 == 0)
                printf("I=%.0lf J=%.0lf\n",i,(i+k));
            else
                printf("I=%.1lf J=%.1lf\n",i,(i+k));
        }
        contador += 1;
        i += 0.2;    
    }

    return 0;
}