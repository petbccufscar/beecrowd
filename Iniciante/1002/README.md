# Problema:

A fórmula para calcular a área de uma circunferência é: area = π . raio2. Considerando para este problema que π = 3.14159.
Efetue o cálculo da área, elevando o valor de raio ao quadrado e multiplicando por π.

**Problema completo**: https://www.urionlinejudge.com.br/judge/pt/problems/view/1002

# Resolução:

O problema pede o cálculo da área de uma circuferência, para obtê-la, devemos declarar e ler os valores para assim calcular a área com a formula informada.

Declaramos então, variaveis do tipo ```c double```  (ponto flutuante de dupla precisão) como requerido pelo enunciado:

```c
        double area, raio, pi;
```

Iremos receber do usuário o valor do ```c raio``` e salvar o resultado em ```c area```. Como os valores podem ser decimais, declaramos com o tipo ```c double``` , para não perdermos informações.

Temos que o valor de ```c pi```  já foi definido pelo problema 
"Considerando para este problema que π = 3.14159" podemos então atribuir esse valor a nossa váriavel ```c pi``` .

```c
        pi = 3.14159;
```


Para leitura, usamos a função ```c scanf``` :
```c
        scanf("%lf",&raio);
```

Utilizamos ```c %lf```  porque estamos recebendo um valor ```c double```  do usuário. 

Agora fazemos uma atribuição a variável ```c area```  seguindo a fórmula de área de uma circunferência.
```c
        area = (raio*raio)*pi;
```
E por fim, escrevemos o resultado na tela utilizando a função ```c printf``` :
```c
        printf("A= %.4lf\n",area);
```

Utilizamos ```c .4```  para a saída ficar com 4 casas de precisão (como mostra nos exemplos de saída do problema).
```c %lf```  será substituido pelo valor contido em ```c area``` .


##### Para aprender um pouco mais sobre variáveis: [Variáveis](http://linguagemc.com.br/variaveis-em-linguagem-c/)

##### Para entender sobre entradas e saídas: [Entrada e Saida](http://linguagemc.com.br/operacoes-de-entrada-e-saida-de-dados-em-linguagem-c/)