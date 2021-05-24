# Problema:

Você tem em mãos dois cabos circulares de energia. O primeiro cabo tem raio R1 e o segundo raio R2. Você precisa comprar um conduite circular (veja a imagem abaixo que ilustra um conduite) de maneira a passar os dois cabos por dentro dele:

![Imagem do exercício](https://resources.urionlinejudge.com.br/gallery/images/problems/UOJ_1589.jpg)

Qual o menor raio do conduite que você deve comprar? Em outras palavras, dado dois círculos, qual o raio do menor círculo que possa englobar ambos os dois?

###### Problema completo: https://www.urionlinejudge.com.br/judge/pt/problems/view/1589

# Resolução

O exercício fornece um determinado número T de casos teste e deseja que, em cada um deles, seja verificado qual o tamanho mínimo da circunferência que é capaz de englobar outras duas (que possuem raios R1 e R2).  

Iniciamos declarando as variáveis que serão utilizadas:

```c
        int T, R1, R2, i;
```
Sendo `T` o número de casos a ser analisado; `R1` e `R2` o valor do raio das circunferências 1 e 2, respectivamente; e `i` responsável pelas iterações no `for`.

Fazemos, então, a leitura de `T` para podermos, posteriormente, trabalhar com a estrutura de repetição `for`:

```c
        scanf("%d", &T);
```
Criamos o `for` e em seu conteúdo a resposta do exercício. 
Fazemos a leitura de `R1` e `R2` e em seguidas printamos sua soma, a qual pode ser feita direta dentro do `prinf`, que irá representar o número mínimo que o raio da circunferência externa terá.

```c
        for (i = 1; i <= T; i++)
        {
                scanf("%d%d", &R1, &R2);
                printf("%d\n", R1+R2);   
        }
```

#### Para aprender um pouco mais sobre: [Estrutura de repetição for](http://linguagemc.com.br/a-estrutura-de-repeticao-for-em-c/)

Caso tenha alguma dúvida sobre este problema ou sobre a resolução, entre em contato com o PET-BCC pelo nosso
[Facebook](https://www.facebook.com/petbcc/),
[Instagram](https://www.instagram.com/petbcc.ufscar/)
ou nos mande um e-mail com o assunto "URI" para petbcc.ufscar@gmail.com


