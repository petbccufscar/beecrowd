# Problema:

O seu professor gostaria que você fizesse um programa com as seguintes características:

1. Crie três variáveis para armazenar números inteiros;
2. Leia o primeiro número, que pode ser um valor na faixa de: -10000 ≤ A ≤ 10000;
3. Leia o segundo número, que pode ser um valor na faixa de: 0 ≤ B ≤ 99;
4. Leia o terceiro número, que pode ser um valor na faixa de: 0 ≤ C ≤ 999;
5. Imprima a letra A, um espaço em branco, o sinal de igual, um espaço em branco, o número armazenado na primeira variável, uma virgula, um espaço em branco, a letra B, um espaço em branco, o sinal de igual, um espaço em branco, o número armazenado na segunda variável, uma virgula, um espaço em branco, a letra C, um espaço em branco, o sinal de igual, um espaço em branco, o número armazenado na terceira variável. Não esqueça de pular linha;
6. Repita o procedimento 5, colocando o número em um espaçamento de 10 dígitos e justificado a direita;
7. Repita o procedimento 5, colocando o número em um espaçamento de 10 dígitos e preenchido com zeros;
8. Repita o procedimento 5, colocando o número em um espaçamento de 10 dígitos e justificado a esquerda.

Exemplo de Entrada:

        1234

        12

        123

Exemplo de Saída:

        A = 1234, B = 12, C = 123

        A =       1234, B =         12, C =        123

        A = 0000001234, B = 0000000012, C = 0000000123

        A = 1234      , B = 12        , C = 123

###### Problema completo: https://www.urionlinejudge.com.br/judge/pt/problems/view/2757

# Resolução

A ideia do exercício é seguir as instruções dadas pelo próprio para conseguir exibir a saída requisitada.

Seguindo as instruções temos:

1. Crie três variáveis para armazenar números inteiros;

```c
        int A, B, C;
```

2. Leia o primeiro número, que pode ser um valor na faixa de: -10000 ≤ A ≤ 10000;
3. Leia o segundo número, que pode ser um valor na faixa de: 0 ≤ B ≤ 99;
4. Leia o terceiro número, que pode ser um valor na faixa de: 0 ≤ C ≤ 999;

```c
       scanf("%d%d%d", &A, &B, &C);
```

5. Imprima a letra A, um espaço em branco, o sinal de igual, um espaço em branco, o número armazenado na primeira variável, uma virgula, um espaço em branco, a letra B, um espaço em branco, o sinal de igual, um espaço em branco, o número armazenado na segunda variável, uma virgula, um espaço em branco, a letra C, um espaço em branco, o sinal de igual, um espaço em branco, o número armazenado na terceira variável. Não esqueça de pular linha:

```c
        printf("A = %d, B = %d, C = %d\n", A, B, C);
```

6. Repita o procedimento 5, colocando o número em um espaçamento de 10 dígitos e justificado a direita:
**OBS:**Nessa etapa se atentar ao formato que o exercício pede, no caso tendo 10 dígitos e justificado a direta, para isso usamos a estrutura `%10d` funciona para qualquer tipo de variável numérica.

```c
        printf("A = %10d, B = %10d, C = %10d\n", A, B, C);
```

7. Repita o procedimento 5, colocando o número em um espaçamento de 10 dígitos e preenchido com zeros;
Para preencher os espaços colocados, no caso 10, com algum número é só colocar ele na frente da quantidade de espaços.

```c
        printf("A = %010d, B = %010d, C = %010d\n", A, B, C);
```
8. Repita o procedimento 5, colocando o número em um espaçamento de 10 dígitos e justificado a esquerda.
Para conseguirmos colocar os 10 dígitos e justificado a esquerda, temos que usar um sinal negativo como se fosse um vetor matemático, invertendo o lado quando negativado.

```c
        printf("A = %-10d, B = %-10d, C = %-10d\n", A, B, C);
```

#### Para aprender um pouco mais sobre: [Formatações de saída](https://pt.wikibooks.org/wiki/Programar_em_C/Entrada_e_saída_simples)

Caso tenha alguma dúvida sobre este problema ou sobre a resolução, entre em contato com o PET-BCC pelo nosso
[Facebook](https://www.facebook.com/petbcc/),
[Instagram](https://www.instagram.com/petbcc.ufscar/)
ou nos mande um e-mail com o assunto "URI" para petbcc.ufscar@gmail.com