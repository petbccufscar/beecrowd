#include <stdio.h>
#include <stdlib.h>

int main() {
    char primeira[100];
    char segunda[100];

    scanf("%[^,],%[^\n]", &primeira, &segunda);

    printf("%s\n", primeira);
    printf("%s\n", segunda);

    return 0;
}