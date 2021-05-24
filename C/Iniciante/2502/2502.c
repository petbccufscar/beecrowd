#include <stdio.h>
#include <string.h>
#include <ctype.h>

int main(){
	int tamCifra, qntLinhas, i, j, k;
	char cifra1[21], cifra2[21], fraseEncriptada[1000];

	while(scanf("%d %d\n", &tamCifra, &qntLinhas) != EOF){
		fgets(cifra1, sizeof(cifra1), stdin);
		fgets(cifra2, sizeof(cifra2), stdin);

        for (i = 0; i < tamCifra ; i++)
		{
			cifra1[i]=tolower(cifra1[i]);
			cifra2[i]=tolower(cifra2[i]);
		}

		for(i=0; i<qntLinhas; i++){
		
			fgets(fraseEncriptada, sizeof(fraseEncriptada), stdin);

			for(j=0; j<strlen(fraseEncriptada); j++){
			
				for(k = 0; k<tamCifra; k++){

					if(fraseEncriptada[j] == cifra1[k])
						fraseEncriptada[j] = cifra2[k];
			
					else if(fraseEncriptada[j] == cifra2[k])
						fraseEncriptada[j] = cifra1[k];

					else if(fraseEncriptada[j] == toupper(cifra1[k]))
						fraseEncriptada[j] = toupper(cifra2[k]);
			
					else if(fraseEncriptada[j] == toupper(cifra2[k]))
						fraseEncriptada[j] = toupper(cifra1[k]);
				} 
			}
		    
		    printf("%s", fraseEncriptada);
	    }

	    printf("\n");	    
	}

	return 0;
}