#include <stdio.h>
#include <stdlib.h>


int main(int argc, char *argv[]) {
    float a, b, c;
    float A, B, C;
    
    scanf("%f %f %f", &a, &b, &c);

    if(a<0||b<0||c<0){
        return 0;
    }
    if(a>=b&&a>=c){
        A=a;
        B=b;
        C=c;
    }
    else if(b>a&&b>=c){
        A=b;
        B=a;
        C=c;
    }
    else if(c>a&&c>b){
        A=c;
        B=a;
        C=b;
    }
    
    if(A >= (B+C)){
        printf("NAO FORMA TRIANGULO\n");
    }

    else if((A*A) == ((B*B) + (C*C))){
        printf("TRIANGULO RETANGULO\n");
    }

    else if((A*A) > ((B*B) + (C*C))){
        printf("TRIANGULO OBTUSANGULO\n");

            if((A==B||B==C||C==A)&&(A!=B||B!=C||C!=A)){
                printf("TRIANGULO ISOSCELES\n");
            }
            
    }

    else if((A*A) < ((B*B) + (C*C))){
        printf("TRIANGULO ACUTANGULO\n");

            if((A==B||B==C||C==A)&&(A!=B||B!=C||C!=A)){
                printf("TRIANGULO ISOSCELES\n");
            }
            if(A==B && B==C){
                printf("TRIANGULO EQUILATERO\n");
            }

    }
    return 0;
}