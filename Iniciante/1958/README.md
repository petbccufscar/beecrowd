# Problema:
Números em ponto flutuante podem ser bastante extensos para mostrar. Nesses casos, é conveniente usar a notação científica.

Você deve escrever um programa que, dado um número em ponto flutuante, mostre este número na notação científica: sempre mostre o sinal da mantissa; sempre mostre 4 casas decimais na mantissa; use o caractere 'E' para separar a mantissa do expoente; sempre mostre o sinal do expoente; e mostre o expoente com pelo menos 2 dígitos.

**Problema Completo**: https://www.urionlinejudge.com.br/judge/pt/problems/view/1958


# Resolução:
Usufruindo do comando de notação científica fornecido pela linguagem C, o exercício em questão torna-se bastante simples.  

Conforme exemplificado pelo enunciado, "a entrada é um número em ponto flutuante de dupla precisão" e, portanto, devemos declarar a variável `X` como sendo do tipo `double`. Para armazenar o valor fornecido na entrada, utilizamos a função `scanf()` tendo como argumento `%lf`.  

```c
double X;
scanf("%lf",&X);
```  

Em seguida, basta equiparmos o `printf()` de acordo com o exigido. Inserindo o código `%E` como argumento, o valor será representado em notação científica seguindo alguns padrões: a mantissa será representada com 6 casas decimais, seguida pelo caractere `E` e o expoente contendo seu sinal. Para adaptarmos ao que foi exigido pelo exercício, precisamos apenas inserir `+.4` entre os dois caracteres '%' e 'E'. Assim, garantimos que o sinal da mantissa será revelado (`+` irá relacionar-se com o sinal do número contido em `X`, seguindo a regra do [jogo de sinais](https://brasilescola.uol.com.br/matematica/jogo-sinais.htm); bem como suas 4 casas decimais.  

```c
printf("%+.4E\n",X);
```


##### Para aprender um pouco mais sobre códigos do comando printf: [Tabelas de valores e unidades em C](http://each.uspnet.usp.br/digiampietri/ACH2023/tabelasemc.html)

##### Para aprender um pouco mais sobre o tipo double: [Números decimais em C](https://www.cprogressivo.net/2012/12/Os-tipos-float-e-double-numeros-decimais-reais-em-C.html)

Caso tenha alguma dúvida sobre este problema ou sobre a resolução, entre em contato com o PET-BCC pelo nosso [Facebook](https://www.facebook.com/petbcc/), [Instagram](https://www.instagram.com/petbcc.ufscar/) ou nos mande um e-mail com o assunto "URI" para  petbcc.ufscar@gmail.com
