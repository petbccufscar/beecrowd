# Problema:
Toorg é o integrante mais sábio do grupo de heróis denominado Os Protetores da Via Láctea. Para qualquer pergunta, ele tem a resposta ideal! Escreva um programa que, dada uma pergunta, informe a resposta de Toorg.

**Problema Completo**: https://www.urionlinejudge.com.br/judge/pt/problems/view/2581


# Resolução:
O objetivo deste exercício é bem simples, basta que seja exibida a "resposta ideal" para cada uma das entradas fornecidas.  

Como primeiro passo, declaramos as variáveis inteiras `i` (que auxiliará na estrutura de repetição a ser utilizada) e `N` (para guardar, através da função `scanf()`, a quantidade de casos de teste). Além disso, precisamos declarar a string `mensagem` para armazenar a pergunta feita. Visto que teremos conhecimento do tamanho desta apenas durante a execução do programa, utilizamos a função `malloc`, da biblioteca `stdlib.h`, para realizar a alocação dinamicamente.

```c
int N, i;
char *mensagem = (char*) malloc(sizeof(char));

scanf("%d",&N);
```  

Em seguida, o comando `for` será responsável por realizar `N` iterações. Em cada uma delas, é feita a leitura de `mensagem`, exibe-se a resposta 'I am Toorg!' e utilizamos a função `fflush()` com `stdin` como parâmetro para zerar o buffer de input.  

```c
for(i=1; i<=N; i++){
  scanf("%s",mensagem);
  printf("I am Toorg!\n");
  fflush(stdin);
}
```  


##### Para aprender um pouco mais sobre strings: [Programar em C/Strings](https://pt.wikibooks.org/wiki/Programar_em_C/Strings)  

##### Para aprender um pouco mais sobre alocação dinâmica: [Alocação Dinâmica em C](http://linguagemc.com.br/alocacao-dinamica-de-memoria-em-c/)  

##### Para aprender um pouco mais sobre limpeza do buffer: [Buffer: o que é, como limpar e funções](https://www.cprogressivo.net/2012/12/Buffer--o-que-e-como-limpar-e-as-funcoes-fflush-e-fpurge.html)



Caso tenha alguma dúvida sobre este problema ou sobre a resolução, entre em contato com o PET-BCC pelo nosso [Facebook](https://www.facebook.com/petbcc/), [Instagram](https://www.instagram.com/petbcc.ufscar/) ou nos mande um e-mail com o assunto "URI" para  petbcc.ufscar@gmail.com
