# Problema 1589:

Você tem em mãos dois cabos circulares de energia. O primeiro cabo tem raio R1 e o segundo raio R2. Você precisa comprar um conduite circular (veja a imagem abaixo que ilustra um conduite) de maneira a passar os dois cabos por dentro dele:

![Imagem do exercício](https://resources.urionlinejudge.com.br/gallery/images/problems/UOJ_1589.jpg)

Qual o menor raio do conduite que você deve comprar? Em outras palavras, dado dois círculos, qual o raio do menor círculo que possa englobar ambos os dois?

###### Problema completo: https://www.urionlinejudge.com.br/judge/pt/problems/view/1589

# Resolução

O exercício então consiste em um determinado número T de casos, verificar o tamanho mínimo da circunferência para caber duas outras com raios medindo R1 e R2.   

Iniciamos declarando as variáveis que serão utilizadas:

```c
        int T, R1, R2, i;
```
Sendo `T` o número de casos a ser analisado, `R1` número do raio da circunferência 1, `R2` número do raio da circunferência 2 e `i` responsável pelas iterações no `for`.

Fazemos a leitura do `T` para podermos posteriormente iniciar o `for`:

```c
        scanf("%d", &T);
```
Criamos o `for` e em seu conteúdo a resposta do exercício: 

```c
        for (i = 1; i <= T; i++)
        {
                scanf("%d%d", &R1, &R2);
                printf("%d\n", R1+R2);   
        }
```
Fazemos a leitura de `R1` e `R2` e em seguidas printamos sua soma que irá representar o número mínimo que o raio da circunferência externa terá.

Caso tenha alguma dúvida sobre este problema ou sobre a resolução, entre em contato com o PET-BCC pelo nosso
[Facebook](https://www.facebook.com/petbcc/),
[Instagram](https://www.instagram.com/petbcc.ufscar/)
ou nos mande um e-mail com o assunto "URI" para petbcc.ufscar@gmail.com


