# Problema:
O seu professor gostaria de fazer um programa com as seguintes características:

1. Leia os dados de um CPF no formato XXX.YYY.ZZZ-DD;
2. Imprima os quatro números, sendo um valor por linha.

**Problema Completo**: https://www.urionlinejudge.com.br/judge/pt/problems/view/2763


# Resolução:
O exercício consiste em realizar o armazenamento da entrada separadamente, para que seja possível exibi-la em linhas diferentes, seguindo o padrão do CPF.  

Como primeiro passo, declaramos as variáveis inteiras `X`, `Y`, `Z` e `D`. Estas armazenarão, através da função `scanf()`, cada uma das 4 partes do documento, ou seja, os valores que estão entre os pontos (.) e o traço (-).  

```c
int X, Y, Z, D;

scanf("%d.%d.%d-%d", &X, &Y, &Z, &D);
```  

Para a exibição na tela, é importante atentar-se que os números devem ser expostos de acordo com a estrutura do CPF, ou seja, 11 dígitos distribuídos no formato "XXX.YYY.ZZZ-DD". Como o armazenamento do tipo `int` desconsidera zeros a esquerda, precisaremos inserir argumentos específicos na função `printf()`: `%03d` garantirá que o inteiro contenha 3 dígitos, adicionando zeros à esquerda quando necessário; enquanto `%02d` atuará do mesmo modo, assegurando a representação com 2 dígitos.  

```c
printf("%03d\n",X);
printf("%03d\n",Y);
printf("%03d\n",Z);
printf("%02d\n",D);
```    


Caso tenha alguma dúvida sobre este problema ou sobre a resolução, entre em contato com o PET-BCC pelo nosso [Facebook](https://www.facebook.com/petbcc/), [Instagram](https://www.instagram.com/petbcc.ufscar/) ou nos mande um e-mail com o assunto "URI" para  petbcc.ufscar@gmail.com
