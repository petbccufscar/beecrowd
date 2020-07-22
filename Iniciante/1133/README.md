# Problema:    
Escreva um programa que leia 2 valores X e Y e que imprima todos os valores entre eles cujo resto da divisão dele por 5 for igual a 2 ou igual a 3.

**Problema completo**: https://www.urionlinejudge.com.br/judge/pt/problems/view/1133


# Resolução:
Para resolver o exercício, devemos percorrer todos os números entre `X` e `Y` e calcular o resto da divisão por 5. Se o resto for igual a 2 ou 3, devemos exibir o número na tela.  
Mais precisamente, percorremos os valores entre `X+1` e `Y-1`, já que o exercício pede os números **entre** X e Y. 

Começamos declarando as variáveis de entrada `X` e `Y`, uma variável `i` para utilizar no loop.
```c
int X, Y, i;
```

Fazemos a leitura dos valores `X` e `Y`.
```c
scanf("%d %d", &X, &Y);
```

O exercício avisa que as entradas não necessariamente estão em ordem crescente. Ou seja, poderíamos ler 18 e 10 ao invés de 10 e 18, como no exemplo dado. Por isso, devemos verificar se `X > Y` ou `Y > X`, para começar o loop sempre do menor número.

No caso `X > Y`, iniciamos o loop do menor para o maior, indo de `i = Y+1` até `i < X`.  
Para cada número nesse intervalo, verificamos se o resto da divisão por 5 é igual a 2 ou 3.  
O código que faz essa verificação é `i % 5 == 2 || i % 5 == 3`, usando o operador `%` para calcular o resto da divisão.  
Caso o valor atenda ao requisito, imprimimos `i` na tela com a função `printf()`.

```c
if(X > Y)
    for(i = Y+1; i <= X; i++)
        if(i % 5 == 2 || i % 5 == 3)
            printf("%d\n", i);
```

O caso `Y > X` é análogo, sendo que o loop vai de `i = X+1` até `i < Y`.  
Devemos sempre lembrar de pular uma linha ao final de cada saída, algo exigido pelo URI. Fazemos isso com `\n` no final de toda função `printf()`.

```c
else if(Y > X)
    for(i = X+1; i <= Y; i++)
        if(i % 5 == 2 || i % 5 == 3)
            printf("%d\n", i);
```

###### Note que, como as diretivas possuem apenas uma linha dentro de cada, podemos omitir as chaves `{}`. Em códigos maiores, esta sintaxe não é recomendada.

##### Para revisar o operador %: [Resto de uma divisão inteira](http://linguagemc.com.br/resto-de-uma-divisao-inteira-em-c/)
##### Para relembrar sobre o laço for: [O comando for](http://linguagemc.com.br/a-estrutura-de-repeticao-for-em-c/)
    
Caso tenha alguma dúvida sobre este problema ou sobre a resolução, entre em contato com o PET-BCC pelo nosso
[Facebook](https://www.facebook.com/petbcc/),
[Instagram](https://www.instagram.com/petbcc.ufscar/)
ou nos mande um e-mail com o assunto "URI" para  petbcc.ufscar@gmail.com
