# Problema:   

Robbie é um robô muito carismático, e uma das coisas que ele mais gosta de fazer, além de brincar com Glória, é colecionar moedas. Robbie possui várias moedas com valores iguais ou diferente, e de mesmo mesmo tamanho. e elas são guardadas de maneira organizada uma sobre a outra dentro de um cilindro de vidro. Robbie sempre faz um joguinho com Glória usando suas moedas quando ela pede pra brincar com ele de esconde-esconde, ou quando ela pede pra ele levá-la para passear. O jogo acontece da seguinte maneira: Glória escolhe um número N que será o salto das moedas que serão somadas, então a cada Nmoedas o valor Vi da moeda é somado até que não haja mais moedas, ou seja, Σ de ((VM-(N*0))+(VM-(N*1))+(VM-(N*2) )...), M é o número de moedas. Por exemplo, se existirem 5 moedas com os valores 1, 2 , 3, 4 e 5, e Glória escolher 2 como valor do salto, então serão somadas as moedas 5, 3 e 1, resultando em 9, ao final Robbie verifica se a soma dessas moedas é um número primo, se isso acontecer ele faz o que a Glória quer, caso contrário, a garotinha convence Robbie a jogar novamente, pois ela sempre consegue convencer ele de tudo, alegando que deixará de contar histórias pra ele, caso ele não faça a vontade dela.  

Você como um bom programador da U.S. Robots, ajudará esses dois amigos, escrevendo um programa irá dizer o resultado do jogo.

**Problema Completo**: https://www.urionlinejudge.com.br/judge/pt/problems/view/2709

# Resolução:

O problema pede para guardarmos uma sequência de `M` moedas. Em seguida, devemos percorrer as moedas de trás para frente, pulando `N` moedas e somando seus valores. Exemplo:

Vetor de moedas: `[1, 2, 3, 4, 5]`

| Pulo  | Soma      | Resultado     |
|-------|-----------|---------------|
| N = 2 | 5 + 3 + 1 | 9 (não primo) |
| N = 3 | 5 + 2     | 7 (primo)     |


No final, devemos verificar se a soma das moedas é um número primo e exibir um texto para cada caso.  

Começamos o código com a função que verifica se um número é primo, mas explicaremos ela ao final da resolução.

```c
int ehPrimo(int numero) { ... }
```

Na função principal, declaramos as variáveis que vamos usar. Como o número máximo de moedas é 20, criamos um vetor `V[20]` e usamos a variável `M` para saber quantas posições estão devidamente preenchidas.

```c
int M, N, i, soma;
int V[20];
```

O código será executado enquanto não houver o fim do arquivo de entrada, ou seja, enquanto a função `scanf()` não retornar `EOF`. Para isso, deixamos a função dentro de um loop `while`. Para cada caso de teste, começamos lendo quantas moedas existem e inicializando a `soma` com 0.

```c
while (scanf("%d", &M) != EOF) {

    soma = 0;
```

Em seguida, salvamos todas as moedas no vetor `V`.

```c
    for (i = 0; i < M; i++) {
        scanf("%d", &V[i]);
    }
```

Recebemos a variável `N`, que indica o salto realizado entre as moedas.

```c
    scanf("%d", &N);
```

Agora, utilizamos uma propriedade da estrutura de repetição `for`: o último parâmetro, usualmente um `i++`, representa quanto o contador aumenta ou diminui. Dessa forma, começamos o loop no final do vetor (`M - 1`) e diminuímos o contador em `N` passos, enquanto este for maior ou igual a 0.

```c
    for (i = M - 1; i >= 0; i -= N) {
        soma += V[i];
    }
```

Tendo o resultado da soma das moedas, verificamos se o número é primo e exibimos os textos que o exercício define.

```c
    if (ehPrimo(soma) == 1) {
        printf("You’re a coastal aircraft, Robbie, a large silver aircraft.\n");
    } else {
        printf("Bad boy! I’ll hit you.\n");
    }

}
```
_______________________________

#### Espera aí, como sabemos se um número é primo?!  

Vamos analisar a função do início do código. Primeiro, recebemos um `numero` inteiro e declaramos um contador `i`.

```c
int ehPrimo(int numero) {
    int i;
```

Faremos duas verificações. A primeira condição que elimina vários valores é se um número é par e diferente de 2. Além disso, o exercício considera o número 1 como primo. Se `numero` atender algum dos casos, retornamos 0.

```c
    if ((numero > 2 && numero % 2 == 0) || numero == 1) {
        return 0;
    }
```

Em seguida, tentamos dividir esse número por vários valores ímpares, começando por 3 e subindo de 2 em 2. Fazemos isso porque, se o número não é par, não vai ser divisível por nenhum outro par. As tentativas terminam na metade do número, já que o maior divisor possível seria a metade dele.  
Para descobrir se um número é divisível por outro, utilizamos o operador `%`, que retorna o resto da divisão. Caso o resto seja 0, `numero` é divisível por `i` e então retornamos 0.

```c
    for (i = 3; i < numero/2; i += 2) {
        if (numero % i == 0) {
            return 0;
        }
    }
```

Se a função não teve retorno em nenhuma dessas verificações, concluímos que o número é primo é retornamos 1.

```c
    return 1;
}
```

##### Para revisar sobre o resto de uma divisão inteira: [Resto divisão inteira](http://linguagemc.com.br/resto-de-uma-divisao-inteira-em-c/)
##### Para aprender mais sobre números primos: [Número Primo](https://pt.wikipedia.org/wiki/N%C3%BAmero_primo)
##### Para conhecer mais sobre a estrutura `for`: [O que é, para que serve e como usar o FOR](https://www.cprogressivo.net/2013/02/O-que-e-para-que-serve-e-como-usar-o-laco-FOR-em-C.html)


Caso tenha alguma dúvida sobre este problema ou sobre a resolução, entre em contato com o PET-BCC pelo nosso
[Facebook](https://www.facebook.com/petbcc/),
[Instagram](https://www.instagram.com/petbcc.ufscar/)
ou nos mande um e-mail com o assunto "URI" para  petbcc.ufscar@gmail.com