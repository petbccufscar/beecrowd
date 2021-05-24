# Problema:
O jogo de dominó tradicional, conhecido como duplo-6, possui 28 peças. Cada peça está dividida em dois quadrados e dentro de cada quadrado há entre 0 e 6 círculos. O jogo é chamado de duplo-6 justamente porque esse é o maior número de círculos que aparece num quadrado de uma peça. A figura ao lado mostra uma forma de organizar as 28 peças do jogo duplo-6 em 7 linhas. Essa figura permite ver claramente quantas peças haveria num jogo de dominó, por exemplo, do tipo duplo-4: seriam todas as peças das 5 primeiras linhas, 15 peças no total. Também poderíamos ver, seguindo o padrão da figura, quantas peças possui o jogo de dominó conhecido como mexicano, que é o duplo-12. Seriam 91 peças, correspondendo a 13 linhas. Para a nossa sorte, existe uma fórmula com a qual podemos calcular facilmente o número de peças de um jogo do tipo duplo-N, para um número N natural qualquer: ((N+1)*(N+2))/2. Neste problema, estamos precisando da sua ajuda para escrever um programa que, dado o valor N, use esta fórmula para calcular e imprimir quantas peças existem num jogo de dominó do tipo duplo-N.

**Problema Completo**: https://www.urionlinejudge.com.br/judge/pt/problems/view/3046


# Resolução:

De início, declaramos as variáveis, ambas do tipo `int`, que usaremos na resolução: `duplo_N` que receberá o valor natural representando o tipo do jogo de dominó; `pecas_existentes` que receberá o valor representando quantas peças existem no jogo de dominó em questão.
``` c
    int duplo_N, pecas_existentes;
```

Agora, através da função `scanf` leremos o tipo de dominó e atribuiremos esse valor à `duplo_N`. 
``` c
    scanf("%d", &duplo_N);
```

Desse modo, com o valor obtido, usaremos a fórmula dada no enunciado do problema (((N+1)*(N+2))/2), para fazer o cálculo da quantidade de peças do jogo, e a atribuíremos à `pecas_existentes`.
``` c
    pecas_existentes = (((duplo_N + 1) * (duplo_N + 2)) / 2);
```

Por fim, através da função `printf`, imprimimos o valor das peças que existem, fornecendo a saída requerida pelo problema. Ademais, colocamos o `return 0` para evitar problemas com o corretor do URI.
``` c
    printf("%d\n", pecas_existentes);
    return 0;
```

Caso tenha alguma dúvida sobre este problema ou sobre a resolução, entre em contato com o PET-BCC pelo nosso
[Facebook](https://www.facebook.com/petbcc/),
[Instagram](https://www.instagram.com/petbcc.ufscar/)
ou nos mande um e-mail com o assunto "URI" para  petbcc.ufscar@gmail.com
