# Problema:
Escreva um programa que leia um valor inteiro N. Este N é a quantidade de linhas de saída que serão apresentadas na execução do programa.


**Problema Completo**: https://www.urionlinejudge.com.br/judge/pt/problems/view/1142


# Resolução:
O exercício resume-se a decifrar a relação entre a entrada e saída(padrão) exemplificada e, então, ler um valor inteiro N e reproduzir tal padrão N vezes. Analisando os valores fornecidos(entrada x saída), é possível notar que o padrão de saída é:

** `numero`  `numero`+1 `numero`+2 PUM ** 

Com o valor inicial de `numero` sendo 1 e, ao fim de cada linha, `numero` é acrescido em 4. 

Para realizar isso, declara-se as variáveis inteiras `N`, `i` e `numero`. Inicializa-se `numero` com 1.

```c
int N;
int i;
int numero = 1;

```
Em seguida, lê-se o valor de `N`, por meio da função `scanf()`.

```c
scanf("%d",&N);
```

Em seguida, vamos utilizar a estrutura de repetição `for` para reproduzir N linhas de saída, conforme o padrão decifrado. A cada iteração do laço de repetição, imprimimos a saída na tela utilizando a função `printf()` e, logo após isto, incrementamos o valor de `numero` em 4.  

```c
for(i = 1; i <= N; i++)	{
    printf("%d %d %d PUM\n", numero, numero + 1, numero + 2);
    numero = numero + 4;
  }
```

##### Para aprender um pouco mais sobre a estrutura for: [O que é e como usar o laço FOR](https://www.cprogressivo.net/2013/02/O-que-e-para-que-serve-e-como-usar-o-laco-FOR-em-C.html)  

Caso tenha alguma dúvida sobre este problema ou sobre a resolução, entre em contato com o PET-BCC pelo nosso [Facebook](https://www.facebook.com/petbcc/), [Instagram](https://www.instagram.com/petbcc.ufscar/) ou nos mande um e-mail com o assunto "URI" para  petbcc.ufscar@gmail.com
