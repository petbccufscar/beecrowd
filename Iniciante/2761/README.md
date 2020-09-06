# Problema:
O seu professor gostaria de fazer um programa com as seguintes características:

1. Crie uma variável inteira;
2. Crie uma variável real de simples precisão;
3. Crie uma variável que armazene um carácter;
4. Crie uma variável que armazene uma frase de no máximo 50 caracteres;
5. Leia todas as variáveis na ordem da forma criada;
6. Imprima todas as variáveis como foram lidas;
7. Imprima as variáveis, separando-as por uma tabulação (8 espaços), na ordem que foram lidas;
8. Imprima as variáveis com exatos 10 espaços.

**Problema Completo**: https://www.urionlinejudge.com.br/judge/pt/problems/view/2761


# Resolução:
Para resolução deste exercício, basta que declaremos as variáveis conforme os tipos determinados nos itens 1 a 4 (`int`, `float`, `char` e `char` com tamanho 50) e, após a leitura, realizemos a exibição na tela seguindo as exigências dos itens 7 e 8. Nesta última parte, é necessário ter conhecimento de que a tabulação corresponde ao comando `\t`, equivalente a 8 espaços; e, também, a forma de aplicar-se 10 espaços entre as variáveis.  

Iniciamos com a declaração de `A` (inteiro), `B` (real de simples precisão, ou seja, `float`), `C` (caractere único) e `D` (vetor de caracteres com 50 posições).  

```c
int A;
float B;
char C, D[50];
```  

Tendo feita a alocação em memória, realizamos a leitura através da função `scanf()`. A variável inteira será representada pelo argumento `%d`; enquanto a de simples precisão, por `%f`. Como `C` guardará apenas 1 caractere, utilizamos o formato `%c`. Já o vetor, por possuir mais de uma posição, precisa ser especificado como `%s`. Além disso, para que este possa armazenar frases, precisamos incluir `[^\n]` em seu comando, indicando que será feita a leitura até que encontre a quebra de linha (assim garantimos que espaços serão lidos).  

```c
scanf("%d %f %c %[^\n]s",&A,&B,&C,D);
```  

No item 6, exige-se que todas as variáveis sejam impressas do modo como foram lidas. Dessa forma, basta que coloquemos seus argumentos correspondentes na função `printf()`, sem nenhum espaço os separando. Vale destacar que, ainda sim, é preciso acrescentar `\n` ao final e seguir o padrão de saída especificado: exibir o valor de ponto flutuante com 6 casas decimais, ou seja, `%.6f`.  

```c
printf("%d%.6f%c%s\n",A,B,C,D);
```  

Para cumprir o 7º tópico, apenas acrescentamos, no `printf()`, a tabulação `\t` entre cada uma das variáveis.  

```c
printf("%d\t%.6f\t%c\t%s\n",A,B,C,D);
```  

Por fim, realizamos a última exibição na tela estabelecendo 10 espaços entre as variáveis. Isto difere-se do item 6 somente pelo acréscimo do número 10 após cada `%` existente no `printf()`.  

```c
printf("%10d%10.6f%10c%10s\n",A,B,C,D);
```


##### Para aprender um pouco mais sobre tabulação: [A função printf() e alguns caracteres especiais](https://www.cprogressivo.net/2012/11/A-funcao-printf-Caracteres-Especais.html)

Caso tenha alguma dúvida sobre este problema ou sobre a resolução, entre em contato com o PET-BCC pelo nosso [Facebook](https://www.facebook.com/petbcc/), [Instagram](https://www.instagram.com/petbcc.ufscar/) ou nos mande um e-mail com o assunto "URI" para  petbcc.ufscar@gmail.com
