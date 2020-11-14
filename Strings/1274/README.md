# Problema 

Desde que foi lançado oficialmente o Pomekon no Brasil, Dabriel está tentando realizar seu maior sonho: Ser um Mestre Pomekon. Sua meta é conquistar os 151 Pomekons disponíveis. Ele já conseguiu capturar muitos monstrinhos, porém em sua cidade aparecem muitos Pomekons repetidos, fazendo com que ele capture diversas vezes o mesmo Pomekon.

Vendo que sua mochila está bem cheia, Dabriel pediu para que você fizesse um programa de computador que informasse a ele quantos Pomekons faltam para completar a coleção.

###### Problema completo: https://www.urionlinejudge.com.br/judge/pt/problems/view/2174

# Resolução:

Para resolver este problema, iremos comparar o nome de um Pomekon com o de outro recebido anteriormente. Caso os nomes forem diferentes, acrescentamos um Pomekon em nossa pomedex e, ao final, mostramos quantos pomekons diferentes Dabriel possui.

Iremos importar a biblioteca `string.h` para a utilizaçao das funções:
`strcmp`, que serve para comparar duas `strings` e retornar 0, caso elas forem iguais e `-1` ou `1` se
 elas forem diferentes e;
`strcpy`, que copia uma `string` para outra `string`.
```c
#include <string.h>
```

Iniciamos declarando as variáveis:
`pomedex`, é uma matriz de `char`, ou seja, uma lista de `strings` para armazenar os nomes dos pomekons;
`pomekon`, é uma `string` para receber o nome de cada pomekon;
`i` e `topo`, são variáveis inteira que servirão para percorrer a `pomedex` e verificar os pomekons diferentes;
`n`, que serve para sabermos quantos pomekons no total Dabriel já capturou;
`quant`, que serve para contarmos os pomekons diferentes.
```c
char pomedex[151][1001], pomekon[1001];
int i, n, topo=-1, quant=1;
```

Em seguida, iniciamos `topo = -1`, pois ainda não temos nenhum pomekon para comparar e `quant = 1`, porque iremos receber pelo menos 1 pomekon.
```c
topo = -1; 
quant = 1;
```
Recebemos quantidade total `n` de pomekons de Dabiel com o comando `scanf`. E inicializamos um laço de repetição `while`, onde verificaremos todos os `n` pomekons recebidos.
```c
scanf("%d", &n);
	
while(n--){
``` 

Dentro do `while`, com o comando `scanf`, recebemos o nome de um pomekon. Com a estrutura `if-else` verificamos se não temos nenhum pokemon para comparar, ou seja, `topo = -1`. Se esse for o caso, utilizamos o `++topo` para acrescentar 1 ao `topo` e com a função `strcpy` adicionamos o nome do primeiro pomekon na primeira posição da `pomedex`.
```c
scanf("%s", pomekon);
		
if(topo == -1)
	strcpy(pomedex[++topo], pomekon);
```

Caso já tenhamos um ou mais pomekons para comparar (`topo` > -1) iniciamos a variável `i = 0` para ser utilizada no próximo `while` que irá percorrer a `pomedex` e parar caso a função `strcmp` retorne 0, ou seja, o pomekon que esta sendo verificado já existe na `pomedex`.
```c
i=0;

while(i <= topo && strcmp(pomedex[i],pomekon))
	i++;
```

Depois, com outra estrutura `if`, verificamos se o número de pomekons `i` é maior que o número de pomekons presentes na `pomedex` (`topo`), se isso for verdade, então o pomekon recebido é um novo pomekon e adicionamos o nome dele na `pomedex` com o `strcpy` e somamos +1 em `quant`.
```c
if(i>topo){
	strcpy(pomedex[++topo], pomekon);
	quant++;
}
```

Por fim, com o comando `printf` exibimos a quatidade de pomekons que faltam para Dabiel completar a sua `pomedex`.
```c
printf("Falta(m) %d pomekon(s).\n", 151 - quant);
```

##### Para aprender um pouco mais sobre a biblioteca string: [strings](http://linguagemc.com.br/a-biblioteca-string-h/)

Caso tenha alguma dúvida sobre este problema ou sobre a resolução, entre em contato com o PET-BCC pelo nosso
 * [Facebook](https://www.facebook.com/petbcc/),
 * [Instagram](https://www.instagram.com/petbcc.ufscar/)
 * ou nos mande um e-mail com o assunto "URI" para  petbcc.ufscar@gmail.com
