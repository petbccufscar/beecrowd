# Problema:

Escreva um programa que, dado uma sequência de vogais, em um determinado alfabeto alienígena, contabilize, em um texto escrito com o mesmo alfabeto, quantas vogais o mesmo possui.

###### Problema completo: https://www.urionlinejudge.com.br/judge/pt/problems/view/2150

# Resolução:

Para resolver este problema, é necessário contar as vogais presentes em um texto de um alfabeto alíenigenae aprensentar quantas vogais estão presentes nesse texto.

Iremos importar a biblioteca `string.h` que para utilizar a função `strlen` que retorna o tamanho de uma `string`.
```c
#include <string.h>
```

Iniciamos de clarando as variáveis:
`vogais` e `texto`, vetores de `char`, que armazenarão as vogais do alfabeto alienígena e o texto no mesmo alfabeto, respectivamente;
`contaVogais` do tipo `int`, que irá armazenar a quantidade de vogais presentes no texto;
`i` e `j` do tipo `int`, que servirão para iterar entre as letras do texto.
```c
char vogais[40], texto[500];
int contaVogais, i, j;
```  

Em seguida, iniciamos um laço de repetição `while` que servirá para analisarmos a quantidade de vogais em texto alienígena para vários casos. A condição de parada do `while` acontece quando recebemos um fim de arquivo (EOF) ao lermos a próxima sequência de vogais com o `scanf`.
Dentro do laço de repetição, com o comando `fgets` recebemos o `texto` e iniciamos a variável `contaVogais` em 0, pois ainda não contamos nenhuma vogal em `texto`.
```c
while(scanf("%s ", vogais) != EOF){

	fgets(texto, sizeof(texto), stdin);

	contaVogais = 0;
```

Criamos dois loops `for` encadeados. O primeiro irá passar por cada vogal da sequência de `vogais`, já segundo irá iterar por cada letra de `texto`. Com o comando `if`, verificamos se a vogal (`vogal[i]`) está presente em `texto`, se sim adicionamos 1 à `contaVogais`.
```c
for(i=0;i<strlen(vogais); i++){
	for(j=0; j<srtlen(texto); j++){
		if(vogais[i] == texto[j])
			contaVogais++;
	}
}
```

Por fim, após contar todas as `vogais` presentes em `texto`, exibimos a quantidade em `contaVogais`, com o comando `printf`.
```c
printf("%d\n", contaVogais);
```

Caso tenha alguma dúvida sobre este problema ou sobre a resolução, entre em contato com o PET-BCC pelo nosso
 * [Facebook](https://www.facebook.com/petbcc/),
 * [Instagram](https://www.instagram.com/petbcc.ufscar/)
 * ou nos mande um e-mail com o assunto "URI" para  petbcc.ufscar@gmail.com
