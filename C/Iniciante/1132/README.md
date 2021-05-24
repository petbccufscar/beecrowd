# Problema:    
Escreva um algoritmo que leia 2 valores inteiros X e Y calcule a soma dos números que não são múltiplos de 13 entre X e Y, incluindo ambos.

**Problema completo**: https://www.urionlinejudge.com.br/judge/pt/problems/view/1132


# Resolução:
O exercício pede para calcular a soma de números não-múltiplos de 13, entre X e Y. Tomando o exemplo de entrada e saída fornecido, devemos percorrer todos os números entre 100 e 200 e somar os que não são múltiplos de 13. Para isso, faremos um loop de um número ao outro e, dentro do loop, uma verificação para cada número.

Começamos declarando as variáveis de entrada `X` e `Y`, uma variável `i` para utilizar no loop e `soma` para armazenar a soma dos números.
```c
int X, Y, i, soma;
```

Fazemos a leitura dos valores `X` e `Y` e inicializamos `soma` com 0.
```c
scanf("%d %d", &X, &Y);

soma = 0;
```

O exercício avisa que as entradas não necessariamente estão em ordem crescente. Ou seja, poderíamos ler 200 e 100 ao invés de 100 e 200. Por isso, devemos verificar se `X > Y` ou `Y > X`, para começar o loop sempre do menor número.

No caso `X > Y`, iniciamos o loop do menor para o maior, indo de `i = Y` até `i <= X`.  
Para cada número nesse intervalo, verificamos se o valor não é múltiplo de 13 com `i % 13 != 0`. O operador `%` significa "resto da divisão", ou seja, se o resto da divisão de `i` por `13` não for `0`, o número **não é** múltiplo de 13.  
Somamos o valor de `i` na variável `soma`.

```c
if(X > Y)
    for(i = Y; i <= X; i++)
        if(i % 13 != 0)
            soma += i;
```

O caso `Y > X` é análogo, sendo que o loop vai de `i = X` até `i <= Y`.

```c
else if(Y > X)
    for(i = X; i <= Y; i++)
        if(i % 13 != 0)
            soma += i;
```

###### Note que, como as diretivas possuem apenas uma linha dentro de cada, podemos omitir as chaves `{}`. Em códigos maiores, esta sintaxe não é recomendada.

Por fim, exibimos o valor da soma na tela e pulamos uma linha com `\n`, requisito comum do URI.

```c
printf("%d\n", soma);
```

##### Para revisar o operador %: [Resto de uma divisão inteira](http://linguagemc.com.br/resto-de-uma-divisao-inteira-em-c/)
##### Para relembrar sobre o laço for: [O comando for](http://linguagemc.com.br/a-estrutura-de-repeticao-for-em-c/)
    
Caso tenha alguma dúvida sobre este problema ou sobre a resolução, entre em contato com o PET-BCC pelo nosso
[Facebook](https://www.facebook.com/petbcc/),
[Instagram](https://www.instagram.com/petbcc.ufscar/)
ou nos mande um e-mail com o assunto "URI" para  petbcc.ufscar@gmail.com
