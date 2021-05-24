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

Podemos converter o caractere `letra` em um inteiro fazendo uma atribuição simples.

```c
    numero = letra
```

Dessa forma, o valor contido em `numero` será o decimal referente a letra na tabela ASCII. Porém, o exercício nos pede que a saída seja a posição da letra no alfabeto; ou seja, 'A' = 1, 'B' = 2, e assim sucessivamente. Como é possível observar na tabela, o caractere 'A' equivale ao inteiro 65 e, portanto, antes de exibirmos o resultado, faremos um tratamento do valor contido em `numero`.

```c
    numero = numero - 64;
```

Subtraindo 64 de `numero`, temos a posição no alfabeto equivalente ao caractere em questão. É essencial ter sempre em mente que 'A' equivale a 65 e, na verdade, queremos que 'A' = 1. Dessa forma, podemos exibir esse resultado na tela, com a função `printf`.

```c
printf("%d \n",numero);
```



Caso tenha alguma dúvida sobre este problema ou sobre a resolução, entre em contato com o PET-BCC pelo nosso
[Facebook](https://www.facebook.com/petbcc/),
[Instagram](https://www.instagram.com/petbcc.ufscar/)
ou nos mande um e-mail com o assunto "URI" para  petbcc.ufscar@gmail.com
