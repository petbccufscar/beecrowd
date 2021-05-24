#include <stdio.h>
#include <string.h>

int main() {
	char firstWord[20], secondWord[20];
	
	scanf("%s",&firstWord);
	scanf("%s",&secondWord);
	
	if(strcmp(firstWord, secondWord) < 0){
		printf("%s\n",firstWord);
		printf("%s\n",secondWord);
	}
	
	else if(strcmp(firstWord, secondWord) > 0){
		printf("%s\n",secondWord);
		printf("%s\n",firstWord);
	}
	
	return 0;
}
