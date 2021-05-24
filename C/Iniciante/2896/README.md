# Problema

Um supermercado está fazendo uma promoção de venda de refrigerantes. Se um dia você comprar refrigerantes e levar os cascos vazios no dia seguinte, ela troca cada conjunto de K garrafas vazias  por uma garrafa cheia. Um cliente quer aproveitar ao máximo essa oferta e por isso comprou várias garrafas no primeiro dia da promoção. Agora ele quer saber quantas garrafas terá ao final do segundo dia da promoção, se usá-la ao máximo.

Faça um programa para calcular isso.

###### Problema completo: https://www.urionlinejudge.com.br/judge/pt/problems/view/2896

# Resolução

Para resolver o problema, iremos receber a quantidade comprada e quantas garrafas vazias correspondem a uma cheia. Com isso, iremos calcular quantas garrafas cheias o cliente receberá.

Começamos declarando as variáveis que serão utilizadas no exercício, todas do tipo inteiro. Serão elas:
* `casos`, para o número de casos de teste que será lido;
* `compradas`, para a quantidade de garrafas compradas pelo cliente;
* `troca`, para o valor de equivalência entre garrafas vazias e cheias;
* `i`, para o contador da estrutura de repetição.
```c
    int casos, i, compradas, troca;
```

Recebemos a quantidade de casos com a estrutura `scanf`.
```c
    scanf("%d", &casos);
```

Faremos uma estrutura de repetição `while` com a quantidade de casos em autodecremento. 
```c
    while (casos--)
```

Recebemos a quantidade de garrafas compradas e o numero de garrafas vazias com a estrutura `scanf`.
```c
    scanf("%d %d", &compradas, &troca);
```

Inicializamos a variável `contador` com 0, visto que nenhuma entrada foi analisada ainda.
```c
    int contador = 0;
```

Utilizaremos a quantidade de repetição `for` para fazer a conta de quantas garrafas cheias o cliente receberá. 
Para isso, inicializamos a variável `i` com a quantidade de garrafas compradas em `compradas`. A cada iteração do laço de repetição, `contador` será incrementado e a quantidade de garrafas compradas será decrementada no valor de `troca`, para que não seja contado novamente a quantidade já computada. A estrutura terminará quanto a quantidade de garrafas compradas restantes em `i` for insuficiente para trocar por uma cheia, sendo menor que `troca`.
```c
    for (i = compradas; i >= troca; i -= troca)
        contador++;
```

Por fim, exibiremos na tela a quantidade de garrafas que o cliente receberá, somando `contador` (quantidade de vezes que o laço girou) com `i` (o restante de garrafas para troca) com a estrutura `printf`
```c
        printf("%d\n", contador + i);
```

Caso tenha alguma dúvida sobre este problema ou sobre a resolução, entre em contato com o PET-BCC pelo nosso
[Facebook](https://www.facebook.com/petbcc/),
[Instagram](https://www.instagram.com/petbcc.ufscar/)
ou nos mande um e-mail com o assunto "URI" para  petbcc.ufscar@gmail.com