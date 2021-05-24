# Problema

Leia um valor inteiro N que é a quantidade de casos de teste que vem a seguir. Cada caso de teste consiste de dois inteiros X e Y. Você deve apresentar a soma de Y ímpares consecutivos a partir de X inclusive o próprio X se ele for ímpar. Por exemplo:
para a entrada 4 5, a saída deve ser 45, que é equivalente à: 5 + 7 + 9 + 11 + 13
para a entrada 7 4, a saída deve ser 40, que é equivalente à: 7 + 9 + 11 + 13


**Problema completo**: https://www.urionlinejudge.com.br/judge/pt/problems/view/1158

# Resolução

Primeiramente, iremos declarar nossas variáveis. `N` será a quantidade de casos de teste, `X` e `Y` os dois números na entrada, `soma` o resultado da soma dos Y ímpares consecutivos a partir de X e por fim, `i` e `j` os contadores dos loops `for` que virá a seguir.

```c
    int N, i, j, X, Y, soma;
``` 

Tendo a variável declarada, podemos receber quantos casos de teste faremos utilizando a função `scanf` e o `%d` para se referir ao inteiro `N`.

```c
    scanf("%d",&N);
```

Como temos o número de casos armazenado em `N`, fazemos um loop `for` para contar quantos casos de teste já efetuamos. Podemos dividir essa etapa em 3:

1. Recebemos do usuário os dois inteiros `X` e `Y` e zeramos a variável `soma` para o resultado do caso de teste anterior não atrapalhar o atual.
2. Efetuamos o processo de soma (que é o coração do problema)
3. Escrevemos na tela o resultado da soma, armazenado na variável de mesmo nome.

```c
    for(i = 0; i < N; i++){
        scanf("%d %d",&X, &Y);
        soma = 0;
        /*
            [Processo de soma]
        */
        printf("%d\n",soma);
    }
``` 

Focando no processo de soma agora, temos um loop `for` interno que faz uma contagem de 0 a `Y` pois precisamos somar os `Y` próximos números a partir de `X` que sejam ímpares. 

Para a verificação de paridade, utilizamos o condicional `if(X%2 == 1)`, ou seja, se o resto da divisão de `X` por 2 for igual a 1 significa que `X` é impar. 

* Caso `X` seja ímpar, somamos `X` na variável `soma` (`soma += X` é o mesmo que `soma = soma + X`) e pulamos para o próximo ímpar (`X += 2`)  
* Caso `X` seja par (`else`), somamos `X`+1 na variável `soma`, ou seja, o próximo ímpar, e então pulamos para o próximo par, pra sempre cair no `else`
 
```c
    ...
    for(j=0;j<Y;j++){
            if(X%2 == 1){
                soma += X;
                X+=2;
            }
            else{
                soma += X + 1;
                X += 2;
            }
        }
    ...
```

Dessa forma, somaremos apenas os números ímpares e armazenamos na variável `soma`, que escrevemos na tela ao fim do `for` interno com a função `printf`, assim, podemos reutilizá-la zerando-a na próxima iteração do loop.

```c
    for(i = 0; i < N; i++){
        scanf("%d %d",&X, &Y);
        soma = 0;
        for(j=0;j<Y;j++){
            if(X%2 == 1){
                soma += X;
                X+=2;
            }
            else{
                soma += X + 1;
                X += 2;
            }
        }
        printf("%d\n",soma);
    }
```

#### Aprenda um pouco mais sobre operadores e expressões: [Operadores](https://pt.wikibooks.org/wiki/Programar_em_C/Operadores)

Caso tenha alguma dúvida sobre este problema ou sobre a resolução, entre em contato com o PET-BCC pelo nosso
[Facebook](https://www.facebook.com/petbcc/),
[Instagram](https://www.instagram.com/petbcc.ufscar/)
ou nos mande um e-mail com o assunto "URI" para  petbcc.ufscar@gmail.com
