#include <stdio.h>

int main (){
	
	int frangoDisp, bifeDisp, massaDisp;
	int frangoReq, bifeReq, massaReq;
	int resFrango, resBife, resMassa;

	scanf("%d %d %d", &frangoDisp, &bifeDisp, &massaDisp);
	scanf("%d %d %d", &frangoReq, &bifeReq, &massaReq);

	resFrango = frangoDisp - frangoReq;

	if (resFrango > 0)
		resFrango = 0;


	resBife = bifeDisp - bifeReq;
	if (resBife > 0)
		resBife = 0;


	resMassa = massaDisp - massaReq;
	if (resMassa > 0)
		resMassa = 0;

	printf("%d\n", -(resFrango + resBife + resMassa));

	return 0;
}