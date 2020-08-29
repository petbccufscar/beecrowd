# Problema:

O novo prédio da Sociedade Brasileira de Computação (SBC) possui 3 andares. Em determinadas épocas do ano, os funcionários da SBC bebem muito café. Por conta disso, a presidência da SBC decidiu presentear os funcionários com uma nova máquina de expresso. Esta máquina deve ser instalada em um dos 3 andares, mas a instalação deve ser feita de forma que as pessoas não percam muito tempo subindo e descendo escadas.

Cada funcionário da SBC bebe 1 café expresso por dia. Ele precisa ir do andar onde trabalha até o andar onde está a máquina e voltar para seu posto de trabalho. Todo funcionário leva 1 minuto para subir ou descer um andar. Como a SBC se importa muito com a eficiência, ela quer posicionar a máquina de forma a minimizar o tempo total gasto subindo e descendo escadas.

Sua tarefa é ajudar a diretoria a posicionar a máquina de forma a minimizar o tempo total gasto pelos funcionários subindo e descendo escadas.


Exemplo de Entrada:

                    10
                    20
                    30
Saída: 

                    80


###### Problema completo: https://www.urionlinejudge.com.br/judge/pt/problems/view/2670

# Resolução

A ideia do exercício é entender o andar onde irá ficar a cafeteira e baseado nisso compreender também a relação matemática entre os andares e o subir dos andares.

Começamos declarando as variáveis que serão utilizadas:

```c
        int cafe[3]; 
        int A1, A2, A3, i, menor;
```

`cafe[3]` representa o andar onde ficará a cafeteira, ex: `cafe[0]` = primeiro andar. `A1, A2, A3` são as variáveis que representam a quantidade de pessoas em cada andar, `i` variável de iteração do `for`, `menor` variável responsável por armazenar o menor valor do momento.


Passamos para a leitura da quantidade de pessoas que cada andar terá:

```c
       scanf("%d %d %d", &A1, &A2, &A3);
```

Seguimos para a lógica principal do exercício:

```c
        cafe[0] = A2*2 + A3*4;
        cafe[1] = A1*2 + A3*2;
        cafe[2] = A1*4 + A2*2;
```
Sendo `cafe[]` a variável que representa onde a cafeteira está naquele momento, temos então `cafe[0]` cafeteira no primeiro andar. Com isso só nos resta fazer a lógica matemática envolvida no sobe e desce dos andares, lembrando que descer leva 1 minuto e subir também.

Feito o calculo agora temos que escolher entre as posições que a cafeteira `cafe[]` tem o menor valor: 

```c
        menor = cafe[0];

        for (i = 1; i < 3; i++)
        {
          if(menor>cafe[i]){
              menor=cafe[i];
          }
        }

```
Para isso passamos o valor de `cafe[0]` para menor para assim conseguirmos comparar essa posição inicial com a seguinte `cafe[1]`. Dentro do `for` temos o `if` que está fazendo a comparação para nos retornar o menor valor entre as três possíveis posições da cafeteira.

Terminamos com o `printf` da variável `menor` pedida pelo Uri:

```c
       printf("%d\n", menor);
```

Caso tenha alguma dúvida sobre este problema ou sobre a resolução, entre em contato com o PET-BCC pelo nosso
[Facebook](https://www.facebook.com/petbcc/),
[Instagram](https://www.instagram.com/petbcc.ufscar/)
ou nos mande um e-mail com o assunto "URI" para petbcc.ufscar@gmail.com