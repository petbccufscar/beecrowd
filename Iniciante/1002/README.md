# Problema:

A fórmula para calcular a área de uma circunferência é: area = π . raio2. Considerando para este problema que π = 3.14159.
Efetue o cálculo da área, elevando o valor de raio ao quadrado e multiplicando por π.

**Problema completo**: https://www.urionlinejudge.com.br/judge/pt/problems/view/1002

# Resolução:

O problema pede o cálculo da área de uma circuferência, para obtê-la, devemos declarar e ler os valores para assim calcular a área com a formula informada.

Declaramos então, variaveis do tipo `double`  (ponto flutuante de dupla precisão) como requerido pelo enunciado:

```c
        double area, raio, pi;
```

Iremos receber do usuário o valor do `raio` e salvar o resultado em `area`. Como os valores podem ser decimais, declaramos com o tipo `double` , para não perdermos informações.

Temos que o valor de `pi`  já foi definido pelo problema 
"Considerando para este problema que π = 3.14159" podemos então atribuir esse valor a nossa váriavel `pi` .

```c
        pi = 3.14159;
```


Para leitura, usamos a função `scanf` :
```c
        scanf("%lf",&raio);
```

Utilizamos `%lf`  porque estamos recebendo um valor `double`  do usuário. 

Agora fazemos uma atribuição a variável `area`  seguindo a fórmula de área de uma circunferência.
```c
        area = (raio*raio)*pi;
```
E por fim, escrevemos o resultado na tela utilizando a função `printf` :
```c
        printf("A= %.4lf\n",area);
```

Utilizamos `.4`  para a saída ficar com 4 casas de precisão (como mostra nos exemplos de saída do problema).
`%lf`  será substituido pelo valor contido em `area` .


##### Para aprender um pouco mais sobre variáveis: [Variáveis](http://linguagemc.com.br/variaveis-em-linguagem-c/)

##### Para entender sobre entradas e saídas: [Entrada e Saida](http://linguagemc.com.br/operacoes-de-entrada-e-saida-de-dados-em-linguagem-c/)

Caso tenha alguma dúvida sobre este problema ou sobre a resolução, entre em contato com o PET-BCC pelo nosso
[Facebook](https://www.facebook.com/petbcc/),
[Instagram](https://www.instagram.com/petbcc.ufscar/)
ou nos mande um e-mail com o assunto "URI" para  petbcc.ufscar@gmail.com

