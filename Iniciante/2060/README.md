# Problema:

Bino e Cino são colegas inseparáveis. Bino gosta de criar desafios matemáticos para Cino resolver. Desta vez, Bino gerou uma lista de números e perguntou ao Cino quantos números da lista são múltiplos de 2, 3, 4 e 5.

Esse desafio pode parecer simples, porém, quando a lista contém muitos números, Cino se confunde e acaba errando alguns cálculos. Para ajudar Cino, faça um programa para resolver o desafio de Bino.

###### Problema completo: https://www.urionlinejudge.com.br/judge/pt/problems/view/2060

# Resolução

O exercício consiste em gravar o número de vezes que os múltiplos desejados aparecem.

Para isso iniciamos declarando as variáveis que serão utilizadas:

```c
        int N, L, i;
        int mult2 = 0, mult3 = 0, mult4 = 0, mult5 = 0;
```
`N` o número de repetições que o usuário deseja e `L` os valores de possíveis múltiplos a serem testados e `i` variável que será incrementada no `for`.
`mult2, mult3, mult4, mult5` são contadores que iram controlar a quantidade de múltiplo que cada um deles possui.

Fazemos a leitura do `N` no `scanf`:

```c
        scanf("%d", &N);
```

Seguimos para a construção do `for` onde será feito a lógica do exercício:

```c
       for (i = 0; i < N; i++){
        scanf("%d", &L);
        if(L%2==0){
                mult2++;
        }
        if(L%3==0){
                mult3++;
        }
        if(L%4==0){
                mult4++;
        }
        if(L%5==0){
                mult5++;
        }   
        }
```
No `for` temos a leitura dos números de `L` a cada iteração, seguimos para a verificação, que é feita comparando o resto da divisão usando `%`, verifica se ele é múltiplo de algum dos números, e caso for, incrementamos a variável contadora que representa a quantidade de múltiplos daquele determinado número.
Ex: `L=2` resulta no `mult2 = 1` ou `mult2++`.

Finalizamos printado a saída que o uri requisita:

```c
   printf("%d Multiplo(s) de 2\n", mult2);
   printf("%d Multiplo(s) de 3\n", mult3);
   printf("%d Multiplo(s) de 4\n", mult4);
   printf("%d Multiplo(s) de 5\n", mult5);

```


Caso tenha alguma dúvida sobre este problema ou sobre a resolução, entre em contato com o PET-BCC pelo nosso
[Facebook](https://www.facebook.com/petbcc/),
[Instagram](https://www.instagram.com/petbcc.ufscar/)
ou nos mande um e-mail com o assunto "URI" para petbcc.ufscar@gmail.com