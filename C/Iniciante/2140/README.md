# Problema

Gilberto é um famoso vendedor de esfirras na região. Porém, apesar de todos gostarem de suas esfirras, ele só sabe dar o troco com duas notas, ou seja, nem sempre é possível receber o troco certo. Para facilitar a vida de Gil, escreva um programa para ele que determine se é possível ou não devolver o troco exato utilizando duas notas.

As notas disponíveis são: 2, 5, 10, 20, 50 e 100.

###### Problema completo: https://www.urionlinejudge.com.br/judge/pt/problems/view/2140

# Resolução

Para resolver o problema, iremos avaliar todos os possíveis valores que podemos devolver o troco exato, salvar em um vetor e avaliar todos os casos comparando-os com o vetor.

Primeiro iremos declarar nossas variáveis. Como são valores inteiros, serão do tipo `int`. As variáveis serão `N` e `M`, conforme o enunciado, a variavel de troco que o cliente precisa `troco`, o contador da estrutura de repetição `i` e o contador de verificação se é possível ou não `contador`.
```c
    int N, M, troco, i, contador;
```

Teremos, também, o vetor de valores possíveis de troco, com todos os valores aceitáveis.
```c
    int possiveis[15] = {7, 12, 22, 52, 102, 15, 25, 55, 105, 30, 60, 110, 70, 120, 150};
```

Faremos uma estrutura de repetição `while` com condição de parada 1, sendo um loop infinito até que seja quebrado por uma estrutura `break` dentro do loop.
```c
    while(1)
```

Iremos ler as entradas de valor do produto `N` e valor pago pelo cliente `M` com a estrutura `scanf`.
```c
        scanf("%d%d", &N, &M); 
```

Caso os valores lidos sejam ambos 0, saímos do `while` e terminamos o programa
```c
        if(N==0 && M==0) 
            break;
```

Caso não entre na condição de término, calcularemos qual o troco que o cliente precisa receber.
```c
        troco = M - N;
```

Agora, verificaremos todos os valores do vetor de `possiveis` com uma estrutura de repetição `for`. Começamos com o contador como 0, `FALSE` em booleano.
```c
        for(i=0, contador = 0; i<15; i++)
```

Caso encontremos o valor do troco que o cliente precisa de `troco` no vetor de valores possíveis, terminamos a condição colocando o contador como 1, `TRUE` em booleano, e saímos do loop.
```c
            if(possiveis[i] == troco)
                contador = 1;
                break;
```

Caso o contador seja 1, exibimos a mensagem de que é possível dar o troco com a estrutura `printf`.
```c
        if(contador) 
            printf("possible\n");
```

Caso contrário, informamos que não é possível.
```c
        else 
            printf("impossible\n");
```

##### Para aprender mais sobre o uso de 1 ou 0 para booleano: [booleano](https://allanlima.wordpress.com/2006/11/07/simulando-o-tipo-boolean-em-c/)

Caso tenha alguma dúvida sobre este problema ou sobre a resolução, entre em contato com o PET-BCC pelo nosso
* [Facebook](https://www.facebook.com/petbcc/),
* [Instagram](https://www.instagram.com/petbcc.ufscar/)
* ou nos mande um e-mail com o assunto "URI" para  petbcc.ufscar@gmail.com