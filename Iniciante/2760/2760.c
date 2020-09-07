#include <stdio.h>
 
int main() {
 
    char a[101], b[101], c[101];
    int i;
    
    scanf(" %[^\n]", a);
    scanf(" %[^\n]", b);
    scanf(" %[^\n]", c);
    
    printf("%s%s%s\n", a, b, c);
    printf("%s%s%s\n", b, c, a);
    printf("%s%s%s\n", c, a, b);

    for(i=0;i<10;i++) {
        if (a[i] == '\0')
            i = 10;
        else
            printf("%c", a[i]);
    }
    
    for(i=0;i<10;i++) {
        if (b[i] == '\0')
            i = 10;
        else
            printf("%c", b[i]);
    }
            
    for(i=0;i<10;i++) {
        if (c[i] == '\0')
            i = 10;
        else
            printf("%c", c[i]);
    }  
            
    printf("\n");
    
    return 0;
}
