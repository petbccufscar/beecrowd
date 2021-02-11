# Problema:
Uma instituição de ensino lisboeta tem como prática para atribuição de senha de acesso ao portal acadêmico utilizar o RA (registro acadêmico) do aluno. Nesta instituição os RA's são strings de 20 caracteres iniciados sempre pelos caracteres "RA" e seguidos por 18 dígitos numéricos. por exemplo: RA000000000000012340. Estes identificadores são gerados automaticamente pelo sistema de matrículas e são formados por três partes principais: (a) iniciados pelos caracteres "RA", (b) seguidos por Z digitos zeros formatadores de posição (onde, 0 <= Z <= 17), e por fim, (c) o número identificador do aluno propriamente dito, considerando os X números mais a direita do RA não iniciados por zero (onde, 1 <= X <= 18).   

**Problema completo**: https://www.urionlinejudge.com.br/judge/pt/problems/view/2714

# Resolução:

A lógica do problema consiste em analisar uma string conforme os padrões estipulados, conferindo se a mesma atende ou não aos padrões. Ou seja, analisar se seu começo tem "RA", se seu meio possui uma sequência, de um ou mais, zeros e, por fim, se existente, analisar qual é a sequência final de números que representa a senha provisória. 
Antes de mais nada, declara-se as bibliotecas de função que serão usadas. Neste caso: `<stdio.h>` para receber e imprimir dados.
``` c
#include <stdio.h>
```
Agora, dentro da função `main`, declara-se as variáveis necessárias. Do tipo `int`: `quantidade_ra` que receberá quantas entradas serão analisadas; `i`, `j` e `k` que serão contadores. Do tipo `char`(ambas iniciadas vazias): `ra_enviados` que será o vetor para armazenar a entrada de informação; `senha_provisoria` que armazenará a parte correspondente a senha provisória.
``` c
  int quantidade_ra, i, j, k;
  char ra_enviados[100] = {'0'},senha_provisoria[20] = {'0'};
```

Na sequência, deve-se ler, com `scanf`, a quantidade de RA's a serem considerados. Limitado à esse valor, cria-se um loop `for` que se inicia lendo a string que contém os dados do suposto RA em questão.
``` c
  scanf("%d", &quantidade_ra);
  for(i = 0; i < quantidade_ra; i++) {
      scanf("%s", &ra_enviados);
``` 

Prossegue-se então para a análise da string lida. Primeiramente, , através de uma estrutura condicional `if`, confere-se se os dois primeiros elementos(indíce 0 e 1) da string são, respectivamente, "R" e "A", caso não sejam, cria-se uma saída `else` com a impressão da mensagem "INVALID DATA\n". 
``` c
  scanf("%s", &ra_enviados);
      if(ra_enviados[0] == 'R' && ra_enviados[1] == 'A') {
        /* código omitido para
        futura explicação */
      }
      else {
        printf("INVALID DATA\n");
      }
```
Caso o começo da string seja válido, deve-se então analisar se seu meio é composto de zeros. Para tal, com auxílio de `j` sendo configurada para 2 (indíce dos elementos após os dois primeiros), cria-se um loop `while` que acessa cada elemento da string e o compara com '0'. Enquanto forem sendo acessados zeros, `j` será incrementada para se manter o controle de qual e quantos elementos já foram acessados. Após encerrar o primeiro loop, configura-se `k` para 0 e cria-se um novo `while`. Por sua vez, esse laço percorrerá o resto da string até seu final, elemento `'\0'`, copiando cada elemento acessado para `senha_provisoria`. Para tal, `k` serve como controle de acesso a qual índice de `senha_provisoria` deve ser adicionado o elemento em questão e `j` faz o controle de acesso aos elementos de `ra_enviados` a serem copiados. Logo, a cada execução do loop ambas variáveis devem ser incrementadas para atualizar-se os índices de acesso.
``` c
      j = 2;
      while (ra_enviados[j] == '0') {
        j++;
      }
      k = 0;
      while (ra_enviados[j] != '\0') {
        senha_provisoria[k] = ra_enviados[j];
        k++;
        j++;
      }
```
Por fim, confere-se se o tamanha da string analisada corresponde ao tamanho padrão de um RA, 20 caracteres totais. Faz-se isso, através de um `if` que comparará se `j`, correspondente a quantos elementos há na string que foi analisada, é igual a 20. Se sim, a mensagem lida e analisada configura um RA correto. Portanto imprimi-se uma mensagem com os valores presentes em `senha_provisoria`, os mesmos correspondem a senha provisória contida na string analisada. 
``` c
      if(j==20) {
        printf("%s\n", senha_provisoria);
      }
```

Para se encerrar a execução do programa conforme os padrões de correção do URI, insere-se `return 0` finalizando a função `main`.
``` c
  return 0;
}
```

Caso tenha alguma dúvida sobre este problema ou sobre a resolução, entre em contato com o PET-BCC pelo nosso [Facebook](https://www.facebook.com/petbcc/), [Instagram](https://www.instagram.com/petbcc.ufscar/) ou nos mande um e-mail com o assunto "URI" para petbcc.ufscar@gmail.com .
