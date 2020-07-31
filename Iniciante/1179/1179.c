#include <stdio.h>

void ehPar(int *entradas, int *par, int qtdeValores, int *posicaoPar){
	int tamanhoVetor;
	
	if(*posicaoPar < 5){
		par[*posicaoPar] = entradas[qtdeValores];
		*posicaoPar = *posicaoPar + 1;
	}
			
	else{
				
		for(tamanhoVetor=0; tamanhoVetor<5; tamanhoVetor++){
			printf("par[%d] = %d\n",tamanhoVetor,par[tamanhoVetor]);
		}
		
		*posicaoPar = 0;
		par[*posicaoPar] = entradas[qtdeValores];
		*posicaoPar = *posicaoPar + 1;
				
	}
	
}

void ehImpar(int *entradas, int *impar, int qtdeValores, int *posicaoImpar){
	int tamanhoVetor;
	
	if(*posicaoImpar < 5){
		impar[*posicaoImpar] = entradas[qtdeValores];
		*posicaoImpar = *posicaoImpar + 1;
	}
			
	else{
				
		for(tamanhoVetor=0; tamanhoVetor<5; tamanhoVetor++){
			printf("impar[%d] = %d\n",tamanhoVetor,impar[tamanhoVetor]);
		}
		
		*posicaoImpar = 0;
		impar[*posicaoImpar] = entradas[qtdeValores];
		*posicaoImpar = *posicaoImpar + 1;
			
	}
	
}

void imprimeRestante(int *posicaoPar, int *par, int *posicaoImpar, int *impar){
	int i;
	
	for(i=0; i<*posicaoImpar; i++){
		printf("impar[%d] = %d\n",i,impar[i]);
	}
	
	for(i=0; i<*posicaoPar; i++){
		printf("par[%d] = %d\n",i,par[i]);
	}
}

int main() {
	int entradas[15], par[5], impar[5];
	int posicaoPar=0, posicaoImpar=0;
	int qtdeValores;
	
	for(qtdeValores = 0; qtdeValores < 15; qtdeValores++){
		scanf("%d",&entradas[qtdeValores]);
	}
	
	for(qtdeValores = 0; qtdeValores < 15; qtdeValores++){
		
		if(entradas[qtdeValores]%2 == 0){
			ehPar(entradas, par, qtdeValores, &posicaoPar);
		}
		
		else{
			ehImpar(entradas, impar, qtdeValores, &posicaoImpar);
		}
	}
	
	imprimeRestante(&posicaoPar, par, &posicaoImpar, impar);
	
	return 0;
}
