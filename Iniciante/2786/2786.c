#include <stdio.h>
 
int main() {
 
    int L,C,type1,type2;

    scanf("%d %d",&L,&C);

    type1 = (L+L-1)*(C-1)+L;
    type2 = ((L-1)*2) + ((C-1)*2);

    printf("%d\n", type1);
    printf("%d\n", type2);

    return 0;
}