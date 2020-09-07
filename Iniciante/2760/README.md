# Problema:

O seu professor gostaria de fazer um programa com as seguintes características:

    1. Crie 3 variáveis para armazenar uma frase de no máximo 100 caracteres;
    2. Leia uma frase para a primeira variável;
    3. Leia uma frase para a segunda variável;
    4. Leia uma frase para a terceira variável;
    5. Imprima a primeira variável lida no passo 2, a segunda variável lida no passo 3, a terceira variável lida no passo 4. Não esqueça de pular linha;
    6. Imprima a primeira variável lida no passo 3, a segunda variável lida no passo 4, a terceira variável lida no passo 2. Não esqueça de pular linha;
    7. Imprima a primeira variável lida no passo 4, a segunda variável lida no passo 2, a terceira variável lida no passo 3. Não esqueça de pular linha;
    8. Repita o procedimento 5, imprimindo só 10 caracteres de cada variável.

###### Problema completo: https://www.urionlinejudge.com.br/judge/pt/problems/view/2760

# Resolução:
Diferente da maioria dos exercícios do URI, o enunciado passa um algoritmo. Para o exercício, vamos seguir esse algoritmo passo a passo.

Começamos declarando três vetores `a`, `b` e `c` de tamanho 101 do tipo `char` e uma variável auxiliar `i` do tipo `int`: 
```c
  char a[101], b[101], c[101];
  int i;
```
Essa parte representa o passo 1 do exercício. As etapas 2 a 4 pedem a leitura de cada uma dessas variáveis. Aqui usamos a função `scanf`:
```c
  scanf(" %[^\n]", a);
  scanf(" %[^\n]", b);
  scanf(" %[^\n]", c);
```
Aqui `%[\n]` representa que será lido uma string (vetor de caracteres) até o caractere `\n`, que representa a tecla Enter.

O passo 5 pede para escrever os valores `a`, `b` e `c` lidos. Vamos usar o `printf`:
```c
  printf("%s%s%s\n", a, b, c);
```
Os passos 6 e 7 pedem o mesmo que o passo 5, mas em ordens diferentes. Na etapa 6 os valores irão aparecer na ordem `b`, `c` e `a`; na etapa 7 aparecerão na ordem `c`, `a` e `b`:
```c
  printf("%s%s%s\n", b, c, a);
  printf("%s%s%s\n", c, a, b);
```
O passo 8 pede para mostrar na tela apenas os 10 primeiros caracteres de cada string. Entretanto, pode ser que o vetor tenha menos de 10 caracteres. Por isso, vamos usar o laço de repetição `for`:
```c
  for(i=0;i<10;i++) {
    if (a[i] == '\0')
      i = 10;
    else
      printf("%c", a[i]);
  }
```
Aqui usamos um `if` e caso a posição `i` do vetor `a` contenha o valor `\0` (`a[i] == '\0'`), igualamos `i` a 10 e forçamos o fim do laço de repetição; senão ele imprime o caractere na tela. Essa repetição deve ser feita para as variáveis `b` e `c` também:
```c
  for(i=0;i<10;i++) {
    if (b[i] == '\0')
      i = 10;
    else
      printf("%c", b[i]);
  }
  
  for(i=0;i<10;i++) {
    if (c[i] == '\0')
      i = 10;
    else
      printf("%c", c[i]);
  }  
```
##### Para aprender um pouco mais sobre strings: [Strings](http://linguagemc.com.br/string-em-c-vetor-de-caracteres/)
##### Para aprender um pouco mais sobre vetores: [Vetores](http://linguagemc.com.br/vetores-ou-arrays-em-linguagem-c/)
##### Para aprender um pouco mais sobre estruturas de decisão: [Estrutura de decisão](http://linguagemc.com.br/estrutura-de-decisao-if-em-linguagem-c/)
##### Para aprender um pouco mais sobre a estrutura for: [For](http://linguagemc.com.br/a-estrutura-de-repeticao-for-em-c/)

Caso tenha alguma dúvida sobre este problema ou sobre a resolução, entre em contato com o PET-BCC pelo nosso
* [Facebook](https://www.facebook.com/petbcc/),
* [Instagram](https://www.instagram.com/petbcc.ufscar/)
* ou nos mande um e-mail com o assunto "URI" para  petbcc.ufscar@gmail.com


