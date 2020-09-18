# Problema:

Dada uma letra do alfabeto, informe qual a sua posição.

##### Link do problema: https://www.urionlinejudge.com.br/judge/pt/problems/view/2987
 
 
# Resolução:

Declararemos apenas 2 variáveis para esse problema, `numero` que será um inteiro e `letra` que receberá um caractere.

```c
    int numero;
    char letra;
```

Para receber o caractere usaremos a função `scanf` e atribuiremos essa entrada a variável `letra`

```c
    scanf("%c",&letra);
```

Tendo a letra em mãos, precisamos fazer a conversão para o número inteiro que será nossa saída. 
Para isso, utilizaremos a [tabela ASCII](https://www.ime.usp.br/~kellyrb/mac2166_2015/tabela_ascii.html) que em poucas palavras, é uma tabela de conversão universal utilizada em todo computador.

![Tabela ASCII](http://s2.glbimg.com/fEu3dqWDHAo0Gi1rGJin--DMiT4=/695x0/s.glbimg.com/po/tt2/f/original/2015/02/12/imagem28.jpg)

Podemos atribuir converter o caractere `letra` em um inteiro fazendo uma atribuição simples.

```c
    numero = letra
```

Dessa forma, o valor contido em número será o referente a letra na tabela ASCII. Porém, o exercício nos pede que o número seja a posição da letra no alfabeto, ('A' = 1, 'B' = 2 e assim sucessivamente) e como vimos na tabela, o caractere 'A' equivale ao inteiro 65. Portanto, antes de exibir o resultado, faremos um tratamento em `numero`.

```c
    numero = numero - 64;
```

Subtraindo 64 de `numero` temos o equivalente a posição no alfabeto daquele caractere e podemos exibir esse resultado na tela, com a função `printf`. (Tenha sempre em mente que 'A' equivale a 65 e queremos que 'A' = 1)

```c
printf("%d \n",numero);
```



Caso tenha alguma dúvida sobre este problema ou sobre a resolução, entre em contato com o PET-BCC pelo nosso
[Facebook](https://www.facebook.com/petbcc/),
[Instagram](https://www.instagram.com/petbcc.ufscar/)
ou nos mande um e-mail com o assunto "URI" para  petbcc.ufscar@gmail.com
