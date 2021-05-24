#include <stdio.h>

int main() {

    int mult;
    unsigned long int exp;

    scanf("%d %lu", &mult, &exp);

    while (exp != 0 && mult != 0) {
        printf("%lu\n", (exp * mult));
        
        scanf("%d %lu", &mult, &exp);
    }
    
    return 0;
}