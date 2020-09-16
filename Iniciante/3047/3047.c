#include <stdio.h>

int main(int argc, char **argv)
{

    int M, A, B, X;

    scanf("%d %d %d", &M, &A, &B);
    
    X = M - A - B;

    if (X > A && X > B)
        printf("%d\n", X);
    else if (A > B && A > X)
        printf("%d\n", A);
    else
        printf("%d\n", B);

    return 0;

}