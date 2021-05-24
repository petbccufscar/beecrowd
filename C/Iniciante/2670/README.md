# Problema:

O novo prédio da Sociedade Brasileira de Computação (SBC) possui 3 andares. Em determinadas épocas do ano, os funcionários da SBC bebem muito café. Por conta disso, a presidência da SBC decidiu presentear os funcionários com uma nova máquina de expresso. Esta máquina deve ser instalada em um dos 3 andares, mas a instalação deve ser feita de forma que as pessoas não percam muito tempo subindo e descendo escadas.

Cada funcionário da SBC bebe 1 café expresso por dia. Ele precisa ir do andar onde trabalha até o andar onde está a máquina e voltar para seu posto de trabalho. Todo funcionário leva 1 minuto para subir ou descer um andar. Como a SBC se importa muito com a eficiência, ela quer posicionar a máquina de forma a minimizar o tempo total gasto subindo e descendo escadas.

Sua tarefa é ajudar a diretoria a posicionar a máquina de forma a minimizar o tempo total gasto pelos funcionários subindo e descendo escadas.

###### Problema completo: https://www.urionlinejudge.com.br/judge/pt/problems/view/2670

# Resolução

A ideia do exercício é definir o andar onde irá ficar a cafeteira e, baseado nisso, calcular o tempo gasto por todos os funcionários subindo e descendo escadas.

Começamos declarando as variáveis que serão utilizadas:

```c
        int cafe[3]; 
        int A1, A2, A3, i, menor;
```

`cafe[3]` representa o andar onde ficará a cafeteira, ex: `cafe[0]` = primeiro andar. `A1, A2, A3` são as variáveis que representam a quantidade de pessoas em cada andar. A variável `i`  será usada para iteração no `for` e a `menor` será responsável por armazenar o andar com menor tempo gasto subindo e descendo.


Passamos para a leitura da quantidade de pessoas que cada andar terá:

```c
       scanf("%d %d %d", &A1, &A2, &A3);
```

Seguimos para a lógica principal do exercício - vamos calcular quanto tempo os funcionários dos outros andares gastariam se a cafeteira ficar naquele andar.

```c
        cafe[0] = A2*2 + A3*4;
        cafe[1] = A1*2 + A3*2;
        cafe[2] = A1*4 + A2*2;
```

Sendo `cafe[]` a variável que representa posições possíveis da cafeteira, e sabendo que `cafe[0]` significa que a cafeteira está no primeiro andar, fazemos a seguinte conta:
- Funcionários do segundo andar gastam 2 minutos com escada;
- Funcionários do terceiro andar gastam 4 minutos (2 descendo e 2 subindo);
- O tempo total é a quantidade `A2` de funcionários gastando 2 minutos mais a quantidade `A3` gastando 4 minutos;
- Análogo para os andares `cafe[1]` e `cafe[2]`.

Feito o cálculo, temos que escolher qual posição de `cafe[]` em que os funcionários gastam menos tempo com escadas:

```c
        menor = cafe[0];

        if(menor > cafe[1])
                menor = cafe[1];
        else if (menor > cafe[2])
                menor = cafe[2];

```

Para isso, vamos assumir que o valor de `cafe[0]` é o menor e vamos compará-lo com as outras duas posições. Caso nosso `menor` seja maior que alguma posição, trocamos o valor de `menor` para o dessa posição.

Terminamos com o `printf` da variável `menor` pedida pelo URI:

```c
       printf("%d\n", menor);
```

#### Para aprender um pouco mais sobre: [Estrutura de repetição for](http://linguagemc.com.br/a-estrutura-de-repeticao-for-em-c/)

Caso tenha alguma dúvida sobre este problema ou sobre a resolução, entre em contato com o PET-BCC pelo nosso
[Facebook](https://www.facebook.com/petbcc/),
[Instagram](https://www.instagram.com/petbcc.ufscar/)
ou nos mande um e-mail com o assunto "URI" para petbcc.ufscar@gmail.com