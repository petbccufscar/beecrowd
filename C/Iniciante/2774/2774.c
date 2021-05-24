#include <stdio.h>
#include <math.h>

int main() {

	int H, M, QT, i;
	double X[1000000], xMedio, soma, somatorio, sigma;

	while (scanf("%d %d", &H, &M) != EOF) {
	
    	QT = (int)(H*60)/M;		
	    soma = 0;
	    somatorio = 0;
	    
    	for(i = 0; i < QT; i++) {
			scanf("%lf", &X[i]);
			soma += X[i];
		}
	
    	xMedio = soma / QT;
	
    	for(i = 0; i < QT; i++) {
			soma = (X[i]-xMedio);
			soma *= soma;
			somatorio += soma;
		}
		
		sigma = sqrt((somatorio / (QT-1)));
		printf("%.5lf\n", sigma);
	}
	return 0;
}
