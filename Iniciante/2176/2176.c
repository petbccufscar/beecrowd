#include <stdio.h>
#include <string.h>
 
int main() {
 
    char msg[100];
    int bits, i;
    
    bits = 0;

    scanf("%s", msg);

    for (i = 0; i < strlen(msg); i++) {
        if (msg[i] == '1') {
            bits++;
        }
    }

    printf("%s", msg);

    printf("%d\n", (bits % 2));
 
    return 0;
}