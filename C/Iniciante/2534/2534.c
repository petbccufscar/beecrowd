#include <stdio.h>

void insertionSort(int *vetor, int n) {  
    int aux, i, j;  
    for (i=1; i<n; i++) {  
        aux = vetor[i];  
        j = i - 1;  

        while ((j>=0) && (vetor[j]<aux)) {  
            vetor[j+1] = vetor[j];  
            j = j-1;  
        }  
        vetor[j+1] = aux;  
    }  
}  


int main() {
	int n, q, p, i;
 
	while (scanf("%d%d", &n, &q)!=EOF) {
 
		int v[n];
		for (i=0; i<n; i++)
			scanf("%d", &v[i]);
 
	    insertionSort(v, n);
 
		for(i=0;i<q;i++) {
			scanf("%d", &p);
			printf("%d\n", v[p-1]);
		}
	}
	
	return 0;
}
