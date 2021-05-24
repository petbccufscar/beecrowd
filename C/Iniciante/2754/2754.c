#include <stdlib.h>

int main(){

	double real1, real2;

	real1 = 234.345;
	real2 = 45.698;

	printf("%.6lf - %.6lf\n", real1, real2);
	printf("%.0lf - %.0lf\n", real1, real2);
	printf("%.1lf - %.1lf\n", real1, real2);
	printf("%.2lf - %.2lf\n", real1, real2);
	printf("%.3lf - %.3lf\n", real1, real2);

	printf("%e - %.e\n", real1, real2);
	printf("%E - %.E\n", real1, real2);

	printf("%g - %g\n", real1, real2);
	printf("%g - %g\n", real1, real2);

	return 0;
}