# Problema 1759:

Papai Noel está brincando com seus duendes para entretê-los durante a véspera do Natal. A brincadeira consiste nos elfos escreverem números em pedaços de papel e colocarem no gorro do Papai Noel. Após todos terminarem de colocar os números Noel sorteia um papel e aquele número representa quantos "Ho" o Noel deve falar.

Seu trabalho é ajudar o Papai Noel montando um problema que mostre todos os "Ho" que ele deve falar dado o número sorteado.

###### Problema completo: https://www.urionlinejudge.com.br/judge/pt/problems/view/1759

# Resolução

A resolução do exercício consiste em utilizar uma variável para armazenar a entrada e limitar a fala do Papai Noel. Portanto, esta será exibida na tela `N` vezes: "**Ho Ho.. Ho!**". Lembrando que o último "Ho" deve ser seguido de um ponto de exclamação ("!"), resultando em "Ho!".  
Para isso iniciamos declarando as variáveis que serão utilizadas:


```c
        int N, i;
```
`N` representa o número de "Ho" que foi sorteado e `i` variável padrão utilizada no controle do `for`.

Fazemos, então, a leitura de `N` através da função `scanf`:

```c
        scanf("%d", &N);
```

Seguimos para a construção do `for` onde será feito os printes dos "Ho".

Também temos que lembrar que o último "Ho" tem a forma "Ho!" e para fazer com que essa regra seja cumprida usamos um `if`.
No `if` verificamos se `i`, nossa variável de iteração, iterou as n vezes, que no caso esse n = `N` representa o fim do `for` .

```c
        for (i = 1; i <= N; i++)
        {
                if(i==N)
                        printf("Ho!\n");
                else
                        printf("Ho ");
        }
```
#### Para aprender um pouco mais sobre: [Estrutura de repetição for](http://linguagemc.com.br/a-estrutura-de-repeticao-for-em-c/)

Caso tenha alguma dúvida sobre este problema ou sobre a resolução, entre em contato com o PET-BCC pelo nosso
[Facebook](https://www.facebook.com/petbcc/),
[Instagram](https://www.instagram.com/petbcc.ufscar/)
ou nos mande um e-mail com o assunto "URI" para petbcc.ufscar@gmail.com