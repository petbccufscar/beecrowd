#include <stdio.h>

int main() {
	
    double N;
    int notas100=0, notas50=0, notas20=0, notas10=0, notas5=0, notas2=0;
    int moedas1r=0, moedas50=0, moedas25=0, moedas10=0, moedas5=0, moedas1c=0;
    
    scanf("%lf", &N);
    N = N + 0.001;
    
    if(0<=N<=1000000.00){
        printf("NOTAS:\n");
        
        if(N>=100){
            notas100 = (int)(N/100);
            N = N - (100*notas100);
        }
        printf("%d nota(s) de R$ 100.00\n", notas100);
        
        if(N>=50){
            notas50 = (int)(N/50);
            N = N - (50*notas50);
        }
        printf("%d nota(s) de R$ 50.00\n", notas50);
        
        if(N>=20){
            notas20 = (int)(N/20);
            N = N - (20*notas20);
        }
        printf("%d nota(s) de R$ 20.00\n", notas20);
        
        if(N>=10){
            notas10 = (int)(N/10);
            N = N - (10*notas10);
        }
        printf("%d nota(s) de R$ 10.00\n", notas10);
        
        if(N>=5){
            notas5 = (int)(N/5);
            N = N - (5*notas5);
        }
        printf("%d nota(s) de R$ 5.00\n", notas5);
        
        if(N>=2){
            notas2 = (int)(N/2);
            N = N - (2*notas2);
        }
        printf("%d nota(s) de R$ 2.00\n", notas2);
        
        printf("MOEDAS:\n");
        if(N>=1){
            moedas1r = (int)(N/1);
            N = N - (moedas1r);
        }
        printf("%d moeda(s) de R$ 1.00\n", moedas1r);
        
        if(N>=0.50){
            moedas50 = (int)(N/0.50);
            N = N - (0.50*moedas50);
        }
        printf("%d moeda(s) de R$ 0.50\n", moedas50);
        
        if(N>=0.25){
            moedas25 = (int)(N/0.25);
            N = N - (0.25*moedas25);
        }
        printf("%d moeda(s) de R$ 0.25\n", moedas25);
        
        if(N>=0.10){
            moedas10 = (int)(N/0.10);
            N = N - (0.10*moedas10);
        }
        printf("%d moeda(s) de R$ 0.10\n", moedas10);
        
        if(N>=0.05){
            moedas5 = (int)(N/0.05);
            N = N - (0.05*moedas5);
        }
        printf("%d moeda(s) de R$ 0.05\n", moedas5);
        
        if(N>=0.01){
            moedas1c = (int)(N/(0.01));
            N = N - (0.01*moedas1c);
        }
        printf("%d moeda(s) de R$ 0.01\n", moedas1c);
                
    }
    
    return 0;
}
