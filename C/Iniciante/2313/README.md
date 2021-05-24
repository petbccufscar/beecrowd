# Problema:
Dados três valores, verifique se os três podem formar um triângulo. Em caso afirmativo, verifique se ele é escaleno, isósceles ou equilátero e se trata de um triângulo retângulo ou não.
 
##### Link do problema: https://www.urionlinejudge.com.br/judge/pt/problems/view/2313
 
# Resolução:
Para descobrir se é possível fazer um triângulo com determinados tamanhos de lados verificamos se o maior lado é menor que a soma dos outros dois. Validado isso verificamos o tipo de triângulo, sendo eles equilátero (todos os lados iguais), escaleno (todos os lados diferentes) ou isósceles (2 lados iguais, sendo também retângulo se **maior² = intermediario² + menor²**)
 
Antes de criarmos o nosso código principal, iremos criar duas funções que terão como entrada 2 números inteiros e retornaram qual dentre ele é o maior ou o menor.
Iremos utilizar operador ternário para faze-lo. O ternário consiste em, dada uma *expressão lógica* retornamos entre um valor se for verdadeiro ou outro valor se for falso; separando a expressão por `?` e os possíveis valores por `:` entre si.
Obs: No exercício utilizamos ele diretamente no `return` da função, mas não é obrigatório, podemos inserir seu valor em uma variável.
Exemplo:

`<valor> = < expressão lógica > ? (Verdadeiro) : (Falso)`

Lembrando que precisamos identificar o tipo da entrada e que toda função irá retornar algum dado.
 
```c
int max(int num1, int num2)
{
    return (num1 > num2) ? num1 : num2;
}
 
int min(int num1, int num2)
{
    return (num1 < num2) ? num1 : num2;
}
```
 
Após criar as funções, iremos começar o nosso código principal (`main()`).
Primeiro instanciamos as variáveis necessárias, sendo elas:  6 `long long` (para armazenar os valores dos lados `A`, `B` e `C` e para o `maior`, `intermediario` e `menor`)
Começamos lendo os valores dos lados.
 
```c
    long long int A, B, C, maior, intermediario, menor;
    scanf("%lld %lld %lld", &A, &B, &C);
```
 
Obs: Como estamos utilizando um `long long` (que continua sendo um inteiro, mas nesse caso com mais espaço na memória), a maneira de lermos ele também muda, temos que utilizar `%lld` ao invés de `%d`.
 
Após ler iremos utilizar as funções `max()` e `min()` que criamos no início para armazenar em `maior` e `menor`. Já identificado nós podemos identificar o `intermediario`, que é a soma dos 3 lados menos o `maior` e o `menor`.
 
```c
    maior = max(A, max(B, C));
    menor = min(A, min(B, C));
    intermediario = A + B + C - maior - menor;
```
 
Agora só nos resta descobrir o tipo do triângulo.
 
Para descobrir se o triângulo é inválido basta saber ser `maior` é maior ou igual a somas dos outros 2 lados.
 
```c
    if (maior >= intermediario + menor)
        printf("Invalido\n");
```
 
Caso contrário (`else`), iremos identificar seu tipo:
- Se todos forem iguais é Equilátero
- Se todos forem diferentes é Escaleno
- Se 2 forem iguais é Isósceles
    - Se `maior * maior == (intermediario * intermediario + menor * menor)` também será retangular
    - Senão será somente Isósceles
 
Com base no seu tipo, iremos imprimir qual ele é.
 
```c
    else
    {
        if (maior == intermediario && intermediario == menor)
            printf("Valido-Equilatero\n");
        else if (maior != intermediario && intermediario != menor && maior != menor)
            printf("Valido-Escaleno\n");
        else
            printf("Valido-Isoceles\n");
        if (maior * maior == 
           (intermediario * intermediario + menor * menor))
            printf("Retangulo: S\n");
        else
            printf("Retangulo: N\n");
    }
```
 
##### Para aprender um pouco mais sobre o Ternário: [Ternário](http://excript.com/linguagem-c/operador-ternario-c.html)

 
Caso tenha alguma dúvida sobre este problema ou sobre a resolução, entre em contato com o PET-BCC pelo nosso
[Facebook](https://www.facebook.com/petbcc/),
[Instagram](https://www.instagram.com/petbcc.ufscar/)
ou nos mande um e-mail com o assunto "URI" para  petbcc.ufscar@gmail.com
 

