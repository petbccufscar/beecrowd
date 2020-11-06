# Problema:

Textos podem conter mensagens ocultas. Neste problema a mensagem oculta em um texto é composto pelas primeiras letras de cada palavra do texto, na ordem em que aparecem.

É dado um texto composto apenas por letras minúsculas ou espaços. Pode haver mais de um espaço entre as palavras. O texto pode iniciar ou terminar em espaços, ou mesmo conter somente espaços.

###### Problema completo: https://www.urionlinejudge.com.br/judge/pt/problems/view/1272

# Resolução:

Para resolver este problema, iremos receber um texto e encontraremos a mensagem oculta verificando se um caractere não é um espaço e se é a primeira letra de uma palavra, ou seja, possui um cactere de espaço (' ') na posição anterior. 

Iremos importar a biblioteca `string.h` que para utilizar a função `strlen` que retorna o tamanho de uma `string`.
```c
#include <string.h>
```

Iniciamos declarando as variáveis:
`N`, que será a quantidade de textos a serem decifrados;
`i` e `j`, que irão iterar pelos textos;
`texto`, que será o texto a ser decifrado;
`mensagemOculta`, que será a mensagem ocultada no texto.
```c
int N, i, j;
char texto[52], mensagemOculta[52];
```

Recebemos a quantidade de textos a serem decifrados (`N`) através do `scanf` e criamos um laço de repetição `while`, onde iremos encontrar as mensagens ocultadas em cada texto.
```c
scanf("%d ", &N);

while(N>0){
```

Em seguida, utilizamos o comando `fgets` para receber o texto e iniciamos a variável `j` em 0, pois ela servirá para iteramos entre as posições de `mensagemOculta`. Esse comando `fgets` é similar ao `scanf`, mas se diferencia por conseguir receber espaços(' ').
```
fgets(texto, sizeof(texto), stdin);

j = 0;
```

Criamos uma laço de repetição `for` para percorrer cada caracter do texto e com a estrutura `if` verificamos se o caracter `texto[i]` não é uma espaço (' ') e se é a primeira letra do alfabeto, ou seja, o caractere anterior `texto[i-1]` é um espaço. Também, utilizamos o operador lógico ou para verificar se o primeiro caractere do texto é uma letra. Caso essa preposição seja verdadeira adicionamos o caractere na `mensagemOculta` na posição `j` e passamos para a próxima posição `j++`.
```c
for(i = 0; i < strlen(texto)-1; i++){
	
	if(texto[i] != ' ' && (texto[i-1] == ' ' || !i))
		mensagemOculta[j++] = texto[i]; 
}
```

Por fim, adicionamos na posição final de `mensagemOculta` o caractere `\0` que significa que vetor de cacteres acabou, exibimos a `mensagemOculta` com o comando `printf` e o `N` é decrescido para verificar o próximo texto ou finalizar o `while`.
```c
mensagemOculta[j] = '\0';

printf("%s\n", mensagemOculta);
N--;
```

#### Para aprender mais sobre `fgets`: [fgets](https://aprendendoc.wordpress.com/tag/fgets/)
##### Para aprender um pouco mais sobre a biblioteca string: [strings](http://linguagemc.com.br/a-biblioteca-string-h/)

Caso tenha alguma dúvida sobre este problema ou sobre a resolução, entre em contato com o PET-BCC pelo nosso
 * [Facebook](https://www.facebook.com/petbcc/),
 * [Instagram](https://www.instagram.com/petbcc.ufscar/)
 * ou nos mande um e-mail com o assunto "URI" para  petbcc.ufscar@gmail.com