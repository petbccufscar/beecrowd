# Problema 1759:

Papai Noel está brincando com seus duendes para entretê-los durante a véspera do Natal. A brincadeira consiste nos elfos escreverem números em pedaços de papel e colocarem no gorro do Papai Noel. Após todos terminarem de colocar os números Noel sorteia um papel e aquele número representa quantos "Ho" o Noel deve falar.

Seu trabalho é ajudar o Papai Noel montando um problema que mostre todos os "Ho" que ele deve falar dado o número sorteado.

###### Problema completo: https://www.urionlinejudge.com.br/judge/pt/problems/view/1759

# Resolução

A ideia do exercício é usar uma variável de entrada para limitar uma estrutura de repetição e dentro da mesma printar `N` vezes **Ho Ho.. Ho!**, lembrando que o último "Ho" tem que ser seguido do "!" ficando "Ho!".
Para isso iniciamos declarando as variáveis que serão utilizadas:


```c
        int N, i;
```
`N` o número de repetições que o usuário deseja e `i` variável padrão utilizada no controle do `for`.

Fazemos a leitura do `N` no `scanf`:

```c
        scanf("%d", &N);
```

Seguimos para a construção do `for` onde será feito os printes dos "Ho":

```c
        for (i = 1; i <= N; i++)
        {
                if(i==N)
                        printf("Ho!\n");
                else
                        printf("Ho ");
        }
```
Temos que lembrar que o último "Ho" tem a forma "Ho!" e para fazer que essa regra seja cumprida usamos um `if`, no qual a regra a ser contemplada é a do `i` nossa variável iterativa, a qual controla nosso `for` e se ela for igual ao valor de `N` significara que o final da iteração chegou.

Caso tenha alguma dúvida sobre este problema ou sobre a resolução, entre em contato com o PET-BCC pelo nosso
[Facebook](https://www.facebook.com/petbcc/),
[Instagram](https://www.instagram.com/petbcc.ufscar/)
ou nos mande um e-mail com o assunto "URI" para petbcc.ufscar@gmail.com