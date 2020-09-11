# Problema:

Todo ano em abril reúnem-se na casa da dona Chica o Curupira, Boitatá, o Boto cor de rosa (esse em sua forma de homem, já que assim dona chica gosta mais), o Mapinguari e a Iara para se lembrar de seus momentos com Mani, a bela menina de pele branca. E como não poderia ser diferente o prato principal dessa reunião é a mandioca. Cada um deles come de uma a dez porções de mandioca e eles sempre avisam dona Chica com antecedência a respeito de quantas porções irão comer nesse dia. O tamanho da porção de cada um é diferente, mas sempre são os mesmos. As porções são as seguintes (em gramas):

O Curupira come 300

O Boitatá come 1500

O Boto come 600

O Mapinguari 1000

A Iara come 150

Dona chica por sua vez sempre come 225 gramas de mandioca. Cansada de todo ano ter que calcular quanta mandioca preparar ela contactou você para escrever um programa que informe quanta mandioca deve ser preparada em gramas.

**Problema Completo:** https://www.urionlinejudge.com.br/judge/pt/problems/view/2936

# Resolução:

Para resolver este problema, primeiramente devemos declarar as variáveis que serão utilizadas ao longo do exercício em questão. Iniciamos declarando as variáveis que utilizaremos para fazer a leitura do número de porção que cada um come, sendo as seguintes variáveis do tipo inteiro: `Curupira_porcao`, `Boitata_porcao`, `Boto_porcao`, `Mapinguari_porcao`, e `Iara_porcao`.

E são declarada as variáveis que serão utilizadas para armazenar o valor do cálculo realizado, que também são variáveis do tipo inteiro, sendo elas: `Curupira_come`, `Boitata_come`, `Boto_come`, `Mapinguari_come`, `Iara_come`, e `DonaChica_come`.

Além disto, é declarada uma variável chamada `Soma_total` do tipo inteiro, que servirá para armazenas a soma do total de mandioca que todos comem.

```c
int Curupira_come,Boitata_come,Boto_come,Mapinguari_come,Iara_come,DonaChica_come;
int Curupira_porcao,Boitata_porcao,Boto_porcao,Mapinguari_porcao,Iara_porcao;
int Soma_total;
```

Após informarmos as variáveis que serão utilizadas no decorrer do problema, usamos o comando `scanf` para lermos os valores de `Curupira_porcao`, `Boitata_porcao`, `Boto_porcao`, `Mapinguari_porcao`, e `Iara_porcao`.

```c
scanf("%d %d %d %d %d",&Curupira_porcao,&Boitata_porcao,&Boto_porcao,&Mapinguari_porcao,&Iara_porcao);
```

Em seguida, é feito o cálculo da quantidade em gramas de mandioca que cada um come, multiplicando as gramas de mandioca de cada porção pelo número de porções.

```c
Curupira_come = 300 * Curupira_porcao;
Boitata_come = 1500 * Boitata_porcao;
Boto_come = 600 * Boto_porcao;
Mapinguari_come = 1000 * Mapinguari_porcao;
Iara_come = 150 * Iara_porcao;
DonaChica_come = 225;
```

Assim, resta fazer a soma total, para calcular quantas gramas de mandioca precisará ser preparada:

```c
Soma_total = Curupira_come+Boitata_come+Boto_come+Mapinguari_come+Iara_come+DonaChica_come;   
```

E por fim, escrevemos o nosso resultado com o comando `printf`, conforme demonstrado abaixo.

```c
printf("%d\n",Soma_total);
```
