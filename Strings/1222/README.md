# Problema:   
Machado gosta muito de escrever. Já escreveu muitos contos, resenhas, relatos de viagens que fez, além de um pequeno romance. Agora Machado quer participar de um concurso de contos, que tem regras muito rígidas sobre o formato de submissão do conto. As regras do concurso especificam o número máximo de caracteres por linha, o número máximo de linhas por página, além de limitar o número total de páginas. Adicionalmente, cada palavra deve ser escrita integralmente em uma linha (ou seja, a palavra não pode ser separada silabicamente em duas linhas). Machado quer escrever um conto com o maior número de palavras possível, dentro das regras do concurso, e precisa de sua ajuda. Dados o número máximo de caracteres por linha, o número máximo de linhas por página, e as palavras do conto que Machado está escrevendo, ele quer saber o número mínimo de páginas que seu conto utilizaria seguindo as regras do concurso.

**Problema Completo**: https://www.urionlinejudge.com.br/judge/pt/problems/view/1222

# Resolução:

Inicializamos a resolução deste problema incluindo as bibliotecas `stdio.h` e `string.h`, as quais nos fornece, respectivamente, funções de entrada e saída, e funções para trabalharmos com strings.

```c
#include <stdio.h>
#include <string.h>
```

Iremos declarar algumas variáveis, `n` para receber o numero de palavras que será passado, `l` numero de linhas e `c` numero de caracteres. Uma variável, do tipo int, `i`, para usarmos em nosso laço de repetição. variáveis do tipo int `linhas`, `paginas`, `letras`, `tamanho` as quais controlam, respectivamente, a quantidade de linhas da pagina atual, a quantidade de pagina presente, a quantidade de letras na linha atual e uma variável para ao receber uma nova palavra realizar algumas verificações. E por final uma variável do tipo vetor de caracteres, a qual ira armazenar cada nova palavra, esta possuindo tamanho até "70" caracteres, colocamos "71" por conta de um possível `\n`.

```c
	int n, l, c;
	int i;
	int linhas, paginas, letras, tamanho;
	char palavra[71];
```

Em nosso laço principal, usaremos a estrutura `while`, dentro desta iremos realizar iterações enquanto for recebido entrada de novos valores, de numero de palavras, numero máximo de linhas por pagina e o numero máximo de caracteres por linha.

```c
while (scanf("%d %d %d", &n, &l, &c) != EOF) {
	...
}
```

Dentro de nosso laço principal, começamos definindo alguns valores iniciais, como exemplo, definimos o numero de paginas como 1 pois estamos começando, assim como o numero de linhas, pois ainda iremos receber as palavras. Em seguida recebemos a primeira palavra, armazenamos esta em `palavra` e em seguida atribuímos à variável `letras` a quantidade de caracteres, ou seja o tamanho, da palavra que foi armazenada em `palavra`, esse tamanho sera usado para verificar se a quantidade de caracteres em uma linha não excedeu o limite

```c
paginas = linhas = 1;
scanf("%s", palavra);
letras = strlen(palavra);
```

Após recebida a primeira palavra, iremos utilizar outro laço de repetição, dessa vez vamos usar a estrutura `for`, como parâmetro de iteração iremos percorrer com valor de `i` igual a zero até `i < n-1`, importante que vá até `n-1` pois assim iremos estar desconsiderando, do numero de palavras que havia sido falado que será passado, a palavra que já realizamos a leitura. Dentro de nosso laço, realizamos a leitura de cada nova palavra, assim como armazenamos o tamanho desta na variável `tamanho`.

```c
for (i = 0; i < n-1; ++i){
	scanf("%s", palavra);
	tamanho = strlen(palavra);

	...	
}
```

Ainda dentro de nosso laço de repetição, iremos fazer alguma verificações, nosso primeiro condicional `if` ira verificar se o tamanho atual de caracteres, da linhas que estamos trabalhando, quando acrescentamo o tamanho da nova palavra que foi recebida não esta ultrapassando o limite de caracteres por linha, caso não esteja ultrapassando, adicionamos o valor contido em `tamanho` á variável `letras` e também o espaço presente entre as palavras, realizamos isso através da operação `letras += tamanho + 1`. Caso a soma dos valores contidos em `letras` e `tamanho` ultrapasse o limite de caracteres por linha, incrementamos em 1 o valor contido em `linhas`, após isso é feita a verificação se o numero de linhas atuais não é maior que o numero máximo de linhas permitidas por pagina, caso seja maior, incrementamos em 1 o numero de paginas e definimos o numero de linhas com 1; Caso não tenha ultrapassado o numero de linhas por pagina apenas definimos o novo valor presente em `letras` para o tamanha da palavra atual, valor contido em `tamanho`, dessa forma temos que o numero de caracteres dessa nova linha que estamos trabalhando é igual ao tamanho da nova palavra recebida, equivalente a ter "pulado uma linha".

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

Ao final, após ter realizado a leitura e o tratamento para cada nova palavra recebida, imprimimos na tela o numero de paginas resultante, seguindo o padrão exigido pelo concurso

```c
printf("%d\n", paginas);
```
    
Caso tenha alguma dúvida sobre este problema ou sobre a resolução, entre em contato com o PET-BCC pelo nosso
[Facebook](https://www.facebook.com/petbcc/),
[Instagram](https://www.instagram.com/petbcc.ufscar/)
ou nos mande um e-mail com o assunto "URI" para  petbcc.ufscar@gmail.com