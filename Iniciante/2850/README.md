# Problema:
Humberto tem um papagaio muito esperto. Quando está com as duas pernas no chão, o papagaio fala em português. Quando levanta a perna esquerda, fala em inglês. Por fim, quando levanta a direita fala em francês. Nico, amigo de Humberto, ficou fascinado com o animal. Em sua emoção perguntou: “E quando ele levanta as duas?”. Antes que Humberto pudesse responder, o papagaio gritou: “Ai eu caio, idiota!”.

##### Problema completo: https://www.urionlinejudge.com.br/judge/pt/problems/view/2850

# Resolução:

A ideia é fazer um programa que leia qual pata está levantada e responder qual a língua que o papagaio vai falar.

Nesse exercício vamos declarar uma variável do tipo `char`:
```c
  char condicao[15];
```
`condicao` é um vetor que irá guardar qual pata está levantada.

O exercício aborda um caso de leitura em que deve ser lido até o final do arquivo [EOF - End of File](https://pt.wikipedia.org/wiki/EOF). Fazemos a leitura do `condicao` no `scanf` dentro do `while`:
```c
  while (scanf(" %15[^\n]", condicao) != EOF) {
```
Dentro do `while`, fazemos a leitura e comparamos ao EOF, portanto o `while` irá rodar até chegar no final do arquivo. Este é simbolizado pela quebra de linha (`\n`). Para ler o vetor de caracteres usamos `%15[^\n]`, isso indica que serão lidos caracteres até chegar a um `\n` ou até atingir 15 caracteres.

Sabendo qual pata está levantada, podemos saber qual língua o papagaio vai falar. Para isso usamos um `if` e, dentro dele, usamos a função `strcmp` da biblioteca [string.h](http://linguagemc.com.br/a-biblioteca-string-h/):
```c
    if (!strcmp(condicao, "esquerda"))
      printf("ingles\n");
    else if (!strcmp(condicao, "direita"))
      printf("frances\n");
    else if (!strcmp(condicao, "nenhuma"))
      printf("portugues\n");
    else if (!strcmp(condicao, "as duas"))
      printf("caiu\n");
  }
```
O `strcmp` retorna 0 sempre que os dois vetores de caracteres forem iguais. Usar um `!` no `if` significa que, se o retorno de `strcmp` for 0, ele vai realizar os comandos que estão dentro do `if`.

##### Para aprender um pouco mais sobre vetores: [Vetores](http://linguagemc.com.br/vetores-ou-arrays-em-linguagem-c/)
##### Para aprender um pouco mais sobre a estrutura while: [While](http://linguagemc.com.br/o-comando-while-em-c/)

Caso tenha alguma dúvida sobre este problema ou sobre a resolução, entre em contato com o PET-BCC pelo nosso
[Facebook](https://www.facebook.com/petbcc/),
[Instagram](https://www.instagram.com/petbcc.ufscar/)
ou nos mande um e-mail com o assunto "URI" para  petbcc.ufscar@gmail.com
