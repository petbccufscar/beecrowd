#include <stdio.h>

int main(){
    int km;
    float combustivel, km_l;
    scanf("%d %f",&km,&combustivel);
    km_l = km / combustivel;
    printf("%.3f km/l\n",km_l);

    return 0;
}