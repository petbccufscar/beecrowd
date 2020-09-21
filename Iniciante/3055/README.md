# Problema:

João aprendeu na escola que a média de dois números é o valor da soma desses dois números dividido por dois. Ou seja, a média de dois números A e B é M = (A+B)/2 .

A professora contou para João as notas que ele tirou nas duas provas de Geografia. As duas notas são números inteiros entre 0 e 100. João prontamente calculou a média das duas provas, que também resultou em um número inteiro.

Mas João é muito esquecido, e agora não consegue lembrar-se das duas notas que tirou na prova. Ele consegue se lembrar de apenas uma das notas das provas. Por sorte, ele consegue se lembrar também da média entre as duas notas. Você pode ajudar

João a determinar a nota da outra prova?

**Problema Completo:** https://www.urionlinejudge.com.br/judge/pt/problems/view/3055

# Resolução:

Para resolver este problema, primeiramente devemos declarar as variáveis que serão utilizadas ao longo do exercício em questão. Iniciamos declarando as variáveis que utilizaremos para fazer a leitura da nota A, e da Média, sendo respectivamente as seguintes variáveis do tipo inteiro: `Nota_A`, e `Media`.

E também é declarada a variável que será utilizada para armazenar a nota esquecida, ou seja, o resultado do cálculo a ser realizado (Media * 2 - nota_A), que também é uma variável do tipo inteiro, sendo essa variável a `Nota_B`.

Após informarmos as variáveis que serão utilizadas no decorrer do problema, usamos o comando `scanf` para lermos os valores da `Nota_A` e da `Media`.

```c
int Nota_A, Nota_B, Media;
scanf("%d %d",&Nota_A,&Media);
```

Em seguida, utilizando a fórmula fornecida no problema, M=(A+B)/2, fazemos uma manipulação matemática simples deixando da fórmula da seguinte forma: B=2*M-A; E assim é feito o cálculo para sabermos qual é a nota esquecida, no caso, a `Nota_B`.

```c
Nota_B = 2*Media - Nota_A;
```

E por fim, escrevemos o nosso resultado com o comando `printf`, conforme demonstrado abaixo.

```c
printf("%d\n",Nota_B);
```

Caso tenha alguma dúvida sobre este problema ou sobre a resolução, entre em contato com o PET-BCC pelo nosso [Facebook](https://www.facebook.com/petbcc/), [Instagram](https://www.instagram.com/petbcc.ufscar/) ou nos mande um e-mail com o assunto "URI" para  petbcc.ufscar@gmail.com
