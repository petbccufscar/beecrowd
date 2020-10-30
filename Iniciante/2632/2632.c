#include <stdio.h>
#include <string.h>
#include <math.h>

int main() {
 
    int t, level, dano, i;
    float w, h, x, y, xc, yc, raio;
    float distx, disty, pontomediox, pontomedioy;
    char magia[10];
    
    scanf("%d", &t);
    
    for(i=0;i<t;i++) {
        scanf("%f %f %f %f", &w, &h, &x, &y);
        scanf("%s %d %f %f", magia, &level, &xc, &yc);
        
        if (strcmp(magia, "fire") == 0) {
            dano = 200;
            if (level == 1)
                raio = 20;
            else if (level == 2)
                raio = 30;
            else
                raio = 50;
        }
        
        else if (strcmp(magia, "water") == 0) {
            dano = 300;            
            if (level == 1)
                raio = 10;
            else if (level == 2)
                raio = 25;
            else
                raio = 40;
        }
        
        else if (strcmp(magia, "earth") == 0) {
            dano = 400;
            if (level == 1)
                raio = 25;
            else if (level == 2)
                raio = 55;
            else
                raio = 70;
        }
        
        else if (strcmp(magia, "air") == 0) {
            dano = 100;
            if (level == 1)
                raio = 18;
            else if (level == 2)
                raio = 38;
            else
                raio = 60;
        }
        
        distx = 0;
        disty = 0;
        pontomediox = x + w/2;
        pontomedioy = y + h/2;
        
        if (pontomediox - xc >= 0) {
            if (pontomediox - xc - w/2 > 0)
                distx = pontomediox - xc - w/2;
        }
        else {
            if (-pontomediox + xc - w/2 > 0)
                distx = -pontomediox + xc - w/2;
        }
        
        if (pontomedioy - yc >= 0) {
            if (pontomedioy - yc - h/2 > 0)
                disty = pontomedioy - yc - h/2;
        }
        else {
            if (-pontomedioy + yc - h/2 > 0)
                disty = -pontomedioy + yc - h/2;
        }
        
        if (raio * raio >= distx * distx + disty * disty)
            printf("%d\n", dano);
        else
            printf("0\n");
    }
 
    return 0;
}
