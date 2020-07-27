#include <stdio.h>
 
int main() {
    
    int h1, m1, h2, m2, th, tm;
    scanf("%d%d%d%d", &h1, &m1, &h2, &m2);
    
    if ((m1 == m2) && (h1 == h2)) {
        tm = m2 - m1;
        th = 24;
    }
    
    else {   
        if ((m2 - m1) >= 0)
            tm = m2 - m1;
        else {
            m2 = m2 + 60;
            tm = m2 - m1;
            h2--;
        }
        
        if ((h2 - h1) >= 0)
            th = h2 - h1;
        else {
            h2 = h2 + 24;
            th = h2 - h1;
        }
    }    
    printf("O JOGO DUROU %d HORA(S) E %d MINUTO(S)\n", th, tm);
    return 0;
}
