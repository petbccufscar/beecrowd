# Problema:

A Lapônia, na Finlândia, é região mais a norte da União Europeia e o seu habitante mais famoso é naturalmente o Papai Noel, ou Pai Natal, ou Joulupukki (seu nome em Finlandês). Naturalmente nos dias de hoje o Papai Noel recebe, além das tradicionais cartinhas, muitos e-mails de crianças de todo o mundo.

O problema é que Noel pegou um virus denominado Amli.D em seu computador e todas as mensagens que ele deixou como rascunho tiveram o nome dele alterado. O lado bom é que este virus bagunça apenas o nome dele (Joulupukki) trocando por vezes o primeiro caractere, por vezes o último e não raro os dois. Assim, ao invés de "Joulupukki", o nome pode aparecer como "Joulupukka", "SoulupukkA" ou "Toulupukki", entre outras formas.

Assim, sua tarefa aqui será fazer um software que corrija todas as aparições erradas de "Joulupukki" dos rascunhos dos e-mails de Papai Noel. Temos a garantia dos gnomos de que não há nenhuma palavra com mais de 10 caracteres que contenha a substring "oulupukk", mas seja cuidadoso com relação ao ponto final, como "Toulupukki.", por exemplo. Neste caso teremos que considerar 11 caracteres.

##### Problema completo: https://www.urionlinejudge.com.br/judge/pt/problems/view/2025

# Resolução:

O objetivo desse exercício é criar um programa que leia `n` frases e corrija todas as vezes que "Joulupukki" estiver escrito errado. Seguindo os exemplos dados no enunciado, é possível notar que apenas a primeira e a última letras da palavra estão erradas, então vamos encontrar todas as ocorrências de "oulupukk" da frase e substituir a letra anterior e posterior a essa substring.

Vamos usar quatro variáveis, em que três são do tipo `int` e uma é do tipo `char`:
```c
  int n, i, j;
  char frase[101];
```
`n` representa quantos frases serão corrigidas. `i` e `j` são variáveis auxiliares para as estruturas `for` e `while` respectivamente. `frase` é uma string que representa a frase que vai ser analisada.

Precisamos saber quantos casos de teste vão ser realizados. Para isso, vamos usar um `scanf` para ler `n`:
```c
  scanf("%d", &n);
```
Feito isso, podemos começar a leitura e correção das frases. Vamos criar um laço de repetição `for` para fazer `n` testes:
```c
  for(i = 0; i < n; i++) {
    scanf(" %100[^\n]", frase);
```
`%100[^\n]` significa que a leitura da variável será feita até a presença de um `\n` ou até chegar a 100 caracteres. Com a `frase`, vamos procurar as ocorrências de "oulupukk" usando uma estrutura `while`:
```c
    j = 0;
    while (j < strlen(frase) - 8) {
      if ((frase[j] == 'o') && (frase[j+1] == 'u') && (frase[j+2] == 'l') && (frase[j+3] == 'u')
      && (frase[j+4] == 'p') && (frase[j+5] == 'u') && (frase[j+6] == 'k') && (frase[j+7] == 'k')) {
        frase[j-1] = 'J';
        frase[j+8] = 'i';
      }
      j++;
    }
```
Primeiro igualamos `j` a 0 para ler todos os caracteres da `frase`. Aqui usamos a função `strlen` da biblioteca [stdlib.h](http://linguagemc.com.br/a-biblioteca-padrao-da-linguagem-c/) para determinar o tamanho da string `frase`. Na iteração usamos um `if` para determinar se a substring "oulupukk" está na frase. Se estiver, alteramos `frase` modificando o primeiro caractere antes do "o" para "J" e o caractere depois do segundo "k" para "i". Depois de cada comparação incrementamos o valor de `j` para buscar todas as vezes em que aparece "oulupukk" na frase.

Depois de verificar todos os caracteres de `frase`, mostramos a frase corrigida na tela. Para isso usamos a função `printf`:
```c
    printf("%s\n", frase);
  }
```

##### Para aprender um pouco mais sobre a estrutura for: [For](http://linguagemc.com.br/a-estrutura-de-repeticao-for-em-c/)
##### Para aprender um pouco mais sobre a estrutura while: [While](http://linguagemc.com.br/o-comando-while-em-c/)

Caso tenha alguma dúvida sobre este problema ou sobre a resolução, entre em contato com o PET-BCC pelo nosso
[Facebook](https://www.facebook.com/petbcc/),
[Instagram](https://www.instagram.com/petbcc.ufscar/)
ou nos mande um e-mail com o assunto "URI" para  petbcc.ufscar@gmail.com
