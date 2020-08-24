#include <stdio.h>
#include <string.h>

int main(){
	int quantDiaria, quantAlimento, quantVitaminaC, i;
	char alimento[16];

	scanf("%d", &quantDiaria);

	while(quantDiaria != 0){

		quantVitaminaC = 0;

		for(i=0; i<quantDiaria; i++){

			scanf("%d ", &quantAlimento);
			fgets(alimento, sizeof(alimento), stdin);

			if (!strncmp(alimento, "suco de laranja", 15))
				quantVitaminaC += quantAlimento * 120;
			else if (!strncmp(alimento, "morango fresco", 14))
				quantVitaminaC += quantAlimento * 85;
			else if (!strncmp(alimento, "mamao", 5))
				quantVitaminaC += quantAlimento * 85;
			else if (!strncmp(alimento, "goiaba vermelha", 15))
				quantVitaminaC += quantAlimento * 70;
			else if (!strncmp(alimento, "manga", 5))
				quantVitaminaC += quantAlimento * 56;
			else if (!strncmp(alimento, "laranja", 7))
				quantVitaminaC += quantAlimento * 50;
			else if (!strncmp(alimento, "brocolis", 8))
				quantVitaminaC += quantAlimento * 34;
		}

		if(quantVitaminaC>130)
			printf("Menos %d mg\n", quantVitaminaC-130);

		else if(quantVitaminaC<110)
			printf("Mais %d mg\n", 110-quantVitaminaC);

        else
			printf("%d mg\n", quantVitaminaC);

		scanf("%d", &quantDiaria);
	}

	return 0;
}