# Problema

Leia um conjunto não determinado de pares de valores M e N (parar quando algum dos valores for menor ou igual a zero). Para cada par lido, mostre a sequência do menor até o maior e a soma dos inteiros consecutivos entre eles (incluindo o N e M).

###### Problema completo: https://www.urionlinejudge.com.br/judge/pt/problems/view/1101

# Resolução

A ideia principal do exercício é testar a leitura de um número não determinado de dados, dando como ponto de parada uma certa condição que no caso do exercício é quando algum dos valores atribuidos a `M` ou `N` for 0.

Exercício pede dois números inteiros `M` e `N`, `Sum` será a variável onde o valor da soma será atribuída e `aux` é explicado mais a frente na resolução:

```c
        int M, N, Sum, aux;
```
Não é tão explícito, mas o exercício espera que `M` receba o maior valor na hora da leitura dos valores e para garantir isso temos que fazer a verificação usando um `if` e também verificar o caso de parada onde `M` ou `N` podem ser iguais a 0.

O `if` que verifica se `M` é menor que `N` e irá fazer uma troca simples de váriavel utilizando uma váriavel auxiliar inteira chamada de `aux`.

Em seguida temos que utilizar um `for`, pois o exercício pede para a saída ser a sequência do intervalo entre `M` e `N` (ex:
**2 3 4 5 Sum=14**, com M=5 e N=2).

```c
        for(i= N; i<=M; i++){
            Sum = i + Sum;
            printf("%i ", i);
        }
        printf("Sum=%d\n", Sum);
        
        Sum = 0;
 
```
E para finalizar o exercício vem a parte onde irá ser tratado o fator de ser uma leitura de uma quantidade não definida utilizando um ponto de parada e para isso temos como uma solução utilizar `while`:

```c
        while(M>0&&N>0){
            if(M<N){
                aux = N;
                N = M;
                M = aux;
            }
            for(i= N; i<=M; i++){
                    Sum = i + Sum;
                    printf("%i ", i);
            }
            printf("Sum=%d\n", Sum);
            Sum = 0;
            scanf("%d %d", &M, &N);
        }
    
```
Dentro do `while` está sendo feita as mesmas verificações foram explicadas anteriormente.

Caso tenha alguma dúvida sobre este problema ou sobre a resolução, entre em contato com o PET-BCC pelo nosso
[Facebook](https://www.facebook.com/petbcc/),
[Instagram](https://www.instagram.com/petbcc.ufscar/)
ou nos mande um e-mail com o assunto "URI" para petbcc.ufscar@gmail.com

##### Para aprender um pouco mais sobre Operadores Lógicos em C e a Estrutura de Repetição while:
[Operadores Lógicos em C](http://linguagemc.com.br/operadores-logicos-em-c/#:~:text=Os%20operadores%20lógicos%20são%20utilizados,condições%20simples%20em%20expressões%20lógicas.)
[While](http://linguagemc.com.br/o-comando-while-em-c/)

