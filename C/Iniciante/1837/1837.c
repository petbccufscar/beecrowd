#include <stdio.h>
 
int main() {
    int a, b, q, r;
    
    scanf("%d %d", &a, &b);

    r = a % b;
    
    if (r < 0) {
        if (b > 0)
            r = b + r;
        else
            r = -b + r;
    }
        
    
    q = (a - r) / b;
    
    printf("%d %d\n", q, r);
 
    return 0;
}
