# Problema

Uma das formas de calcular a raiz quadrada de um número natural é pelo método das frações periódicas continuadas. Esse método usa como denominador uma repetição de frações. Essa repetição pode ser feita uma quantidade específica de vezes.
Sua tarefa é, dado o número N de repetições, calcular o valor aproximado da raiz quadrada de 2.

###### Problema completo: https://www.urionlinejudge.com.br/judge/pt/problems/view/2166

# Resolução

Para resolver o problema, iremos receber o número de repetições e, com o cálculo exibido pelo problema de [fração contínua](https://pt.wikipedia.org/wiki/Fra%C3%A7%C3%A3o_cont%C3%ADnua), iremos calcular a raiz de 2.

Começamos declarando as variáveis que serão utilizadas no problema, sendo `n` o número de repetições e `raiz` o valor final da raiz. Como são valores com casas decimais, utilizaremos o tipo `double`.
```c
    double n, raiz;
```

Inicializamos o valor em `raiz` como 0, visto que ainda não a calculamos.
```c
    raiz = 0.0;
```

Para ler o número de repetições `n`, utilizaremos a função `scanf`.
```c
    scanf("%lf", &n);
```

Iniciamos nossa estrutura de repetição `while`, que terá como condição de parada o valor de repetições em `n`.
```c
    while(n>0)
```

Agora, faremos o cálculo aproximado da raiz conforme explicado pelo problema. Como devemos calcular a raiz de 2, ela será somada por 2 em cada loop da estrutura. Em seguida, iremos transformar o valor lido em uma fração, que será recursivamente fracionado conforme exibido no enunciado.
```c
        raiz = raiz + 2.0;
        raiz = 1/raiz;
```

Após este cálculo, iremos diminuir uma repetição em `n`, para que o `while` possa verificar se ainda há repetições para continuar o loop.
```c
        n--;
```

Após o cálculo recursivo de frações, iremos somar em um, acordante com o exibido pelo problema. Este passo é feito no final para que ele não torne-se parte do cálculo de frações em `raiz`.
```c
    raiz = raiz + 1.0;
```

Por fim, exibimos o valor da raiz com a estrutura `printf`, utilizando 10 casas decimais.
```c
    printf("%.10lf\n", raiz);
```

Caso tenha alguma dúvida sobre este problema ou sobre a resolução, entre em contato com o PET-BCC pelo nosso
[Facebook](https://www.facebook.com/petbcc/),
[Instagram](https://www.instagram.com/petbcc.ufscar/)
ou nos mande um e-mail com o assunto "URI" para  petbcc.ufscar@gmail.com