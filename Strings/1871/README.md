# Problema:

Um dia o Prof. Humberto José Roberto fez o seguinte questionamento: Se o zero a esquerda de um número não tem valor algum, por que teria em outras posições de um número? Analisando da seguinte forma, ele pede sua ajuda para, ao somar dois valores inteiros, que o resultado seja exibido segundo o raciocínio dele, ou seja, sem os Zeros. Por exemplo, ao somar 15 + 5, o resultado seria 20, mas com esta nova ideia, o novo resultado seria 2, e, ao somar 99 + 6, o resultado seria 105, mas com esta nova ideia, o novo resultado seria 15.

Escreva um programa que, dado dois números inteiros, sem o algarismo zero, some os mesmos e, caso o resultado tenha algum algarismo zero, que os retire antes de exibir.

###### Problema Completo: https://www.urionlinejudge.com.br/judge/pt/problems/view/1871

# Resolução:

Para resolver o problema, começamos daclarando as variáveis que serão usadas, são elas `m` e `n` que são as entradas do programa, `soma` que armazena o resultado de `m` mais `n`, `i` que é o contador de um laço de repetição, `posi` que vai receber a quantidade de caracteres após a conversão de `soma` em uma `string`, essas variáveis são do tipo inteiro, `num` que é um vetor de caracteres de 21 posições, ou seja uma `string`. A seguir se encontra a declaração dessas variáveis.

```c
#include <stdio.h>

int main() {
  
  int m, n, soma, i, posi;
  char num[21];
```

Em seguida é feito um `while` que tem sua condição de parada como 1, com isso estará sempre rodando, receberemos o valor das variáveis `m` e `n`, em seguida tem um `if` que verifica se as duas entradas são iguas a zero, caso sejam, o laço será interrompido por causa do `break`, dessa forma garantimos que o programa terminará. A baixo esta o código.

```c
  while(1){
    scanf("%d %d", &m, &n);

    if(m == 0 && n == 0){
      break;
    }
```

Em seguida temos a soma de `m` e `n`, e a formatação do conteúdo de `soma` em `string` que esta sendo alocado em `num`, e `posi` está recebendo a quantidade de caracteres que tem `num`, essa conversão é feita pela função `sprintf`. Depois colocamos o `\0` na próxima posição de `posi`.

```c
    soma = m + n;
    posi = sprintf(num, "%d", soma);

    num[posi + 1] = '\0';
```

Percorremos o vetor `num` e imprimimos todos os caracteres diferentes de 0, dessa forma finalizamos o exercício.

```c
    for(i = 0; i < posi; i++) {
      if(num[i] != '0') {
        printf("%c", num[i]);
      }
    }
    printf("\n");
  }

  return 0;
}
```

#### Para aprender mais sobre `sprintf`: [sprintf](https://processolinux.wordpress.com/2009/11/26/c-lendo-de-e-para-strings-com-sscanf-sprintf/)

Caso tenha alguma dúvida sobre este problema ou sobre a resolução, entre em contato com o PET-BCC pelo nosso
 * [Facebook](https://www.facebook.com/petbcc/),
 * [Instagram](https://www.instagram.com/petbcc.ufscar/)
 * ou nos mande um e-mail com o assunto "URI" para  petbcc.ufscar@gmail.com