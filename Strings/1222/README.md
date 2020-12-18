# Problema:   
Machado gosta muito de escrever. Já escreveu muitos contos, resenhas, relatos de viagens que fez, além de um pequeno romance. Agora Machado quer participar de um concurso de contos, que tem regras muito rígidas sobre o formato de submissão do conto. As regras do concurso especificam o número máximo de caracteres por linha, o número máximo de linhas por página, além de limitar o número total de páginas. Adicionalmente, cada palavra deve ser escrita integralmente em uma linha (ou seja, a palavra não pode ser separada silabicamente em duas linhas). Machado quer escrever um conto com o maior número de palavras possível, dentro das regras do concurso, e precisa de sua ajuda. Dados o número máximo de caracteres por linha, o número máximo de linhas por página, e as palavras do conto que Machado está escrevendo, ele quer saber o número mínimo de páginas que seu conto utilizaria seguindo as regras do concurso.

**Problema Completo**: https://www.urionlinejudge.com.br/judge/pt/problems/view/1222

# Resolução:

Inicializamos a resolução deste problema incluindo as bibliotecas `stdio.h` e `string.h`, as quais nos fornece, respectivamente, funções de entrada e saída, e funções para trabalharmos com strings.

```c
#include <stdio.h>
#include <string.h>
```

Iremos declarar as seguintes variáveis do tipo inteiro: `n` para receber o número de palavras que será passado, `l` para receber o número de linhas, `c` para receber o número de caracteres, `i` que será utilizado em nosso laço de repetição, além de `linhas`, `paginas`, `letras` e `tamanho`, as quais controlam, respectivamente, a quantidade de linhas da pagina atual, a quantidade de pagina presente, a quantidade de letras na linha atual e uma variável para realizar algumas verificações ao receber uma nova palavra. Também iremos declarar uma variável do tipo vetor de caracteres, a qual irá armazenar cada nova palavra, cujo tamanho máximo é de "70" caracteres e, por isso, colocamos "71" por conta de um possível `\n`.

```c
	int n, l, c;
	int i;
	int linhas, paginas, letras, tamanho;
	char palavra[71];
```

Em nosso laço principal, usaremos a estrutura `while`, em que iremos realizar iterações enquanto for recebido entrada de novos valores, de número de palavras, número máximo de linhas por pagina e o número máximo de caracteres por linha.

```c
while (scanf("%d %d %d", &n, &l, &c) != EOF) {
	...
}
```

Dentro de nosso laço principal,  inicialmente definimos o numero de paginas e o numero de linhas como 1, pois estamos na primeira página e ainda iremos receber as palavras. Em seguida, após recebermos a primeira palavra, armazenamos esta em `palavra` e atribuímos à variável `letras` a quantidade de caracteres desta, ou seja o tamanho, da palavra que foi armazenada em `palavra`. Note que esse tamanho será usado para verificar se a quantidade de caracteres em uma linha não excedeu o limite.

```c
paginas = linhas = 1;
scanf("%s", palavra);
letras = strlen(palavra);
```

Após recebermos a primeira palavra, iremos utilizar uma estrutura de repetição `for`, cujo parâmetro de iteração irá percorrer de `i` igual a zero até `i < n-1`. É importante que vá até `n-1` para assim desconsiderarmos a palavra que já realizamos a leitura do numero de palavras que havia sido lido e armazenado. Dentro de nossa estrutura de repetição, realizamos a leitura de cada nova palavra e armazenamos o tamanho desta na variável `tamanho`.

```c
for (i = 0; i < n-1; ++i){
	scanf("%s", palavra);
	tamanho = strlen(palavra);

	...	
}
```

Ainda dentro de nosso laço de repetição, iremos fazer alguma verificações. Com o condicional `if`, verificamos se o tamanho atual de caracteres da linhas com a qual estamos trabalhando não esta ultrapassa o limite de caracteres por linha, quando acrescentamos o tamanho da nova palavra que foi recebida à esta e, caso não ultrapasse, adicionamos o valor contido em `tamanho` à variável `letras` e também o espaço presente entre as palavras, por meio da operação `letras += tamanho + 1`. Caso a soma dos valores contidos em `letras` e `tamanho` ultrapasse o limite de caracteres por linha, incrementamos em 1 o valor contido em `linhas` e após isso verificamos se o numero de linhas atuais não é maior que o número máximo de linhas permitidas por página. Caso seja maior, incrementamos em 1 o número de páginas e definimos o número de linhas com 1; Caso não tenha ultrapassado o número de linhas por página, apenas definimos o novo valor presente em `letras` para o tamanha da palavra atual, valor contido em `tamanho`, dessa forma temos que o numero de caracteres dessa nova linha que estamos trabalhando é igual ao tamanho da nova palavra recebida, equivalente a ter "pulado uma linha".

```c
	if ((letras + tamanho + 1) <= c){ 
		letras += tamanho + 1;
	}else{
		++linhas;
		if (linhas > l){
			++paginas;
			linhas = 1;
		}
	letras = tamanho;
	}
```

Ao final, após realizarmos a leitura e o tratamento para cada nova palavra recebida, imprimimos na tela o número de páginas resultante, seguindo o padrão exigido pelo concurso

```c
printf("%d\n", paginas);
```
    
Caso tenha alguma dúvida sobre este problema ou sobre a resolução, entre em contato com o PET-BCC pelo nosso
[Facebook](https://www.facebook.com/petbcc/),
[Instagram](https://www.instagram.com/petbcc.ufscar/)
ou nos mande um e-mail com o assunto "URI" para  petbcc.ufscar@gmail.com
