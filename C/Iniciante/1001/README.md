<img src="../../../docs/icon.png" align="right" />

# [1001] - Extremamente Básico

**Link do Problema:** [Extremamente Básico](https://www.urionlinejudge.com.br/judge/pt/problems/view/1001)

## Problema:

Leia 2 valores inteiros e armazene-os nas variáveis A e B. Efetue a soma de A e B atribuindo o seu resultado na variável X. Imprima X conforme exemplo apresentado abaixo. Não apresente mensagem alguma além daquilo que está sendo especificado e não esqueça de imprimir o fim de linha após o resultado, caso contrário, você receberá "Presentation Error".

## Resolução:

Para ler os 2 valores inteiros antes precisamos declará-los como variáveis, para isso fazemos:
```c
int A, B, X;
```
No nosso caso, "var_name" é substituído por A, B e X.

Para leitura, usamos a função scanf:
```c
scanf("%d", &A);
scanf("%d", &B);
```
Utilizamos %d porque estamos recebendo valores inteiros do usuário.


Agora fazemos uma atribuição à variável "X" somando A e B
```c
X = A + B;
```
E, por fim, escrevemos o resultado na tela utilizando a função printf:
```c
printf("X = %d\n", X);
```
%d será substituído pelo valor contido em X.

> Todas as funções utilizadas estão contidas na biblioteca stdio.h, incluída na primeira linha do nosso programa.

## Material Auxiliar
- Para aprender um pouco mais sobre variáveis: [Variáveis](http://linguagemc.com.br/variaveis-em-linguagem-c/)
- Aprenda sobre as variações possíveis em: [Entrada e Saída](http://linguagemc.com.br/operacoes-de-entrada-e-saida-de-dados-em-linguagem-c/)

## Contato

Se você tiver alguma dúvida, sugestão ou precisar de suporte, por favor, sinta-se à vontade para entrar em contato conosco:

- **E-mail:** petbcc.ufscar@gmail.com

Você também pode criar uma **Issue** no [GitHub](https://github.com/petbccufscar/ufscar-planner/issues) para relatar problemas, sugerir melhorias ou contribuir para o desenvolvimento do UFSCar Planner. Estamos sempre abertos para receber feedback e colaboração. Obrigado!
