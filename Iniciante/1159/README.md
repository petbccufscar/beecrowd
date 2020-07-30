# Problema

O programa deve ler um valor inteiro X indefinidas vezes. (O programa irá parar quando o valor de X for igual a 0). Para cada X lido, imprima a soma dos 5 pares consecutivos a partir de X, inclusive o X , se for par. Se o valor de entrada for 4, por exemplo, a saída deve ser 40, que é o resultado da operação: 4+6+8+10+12, enquanto que se o valor de entrada for 11, por exempo, a saída deve ser 80, que é a soma de 12+14+16+18+20.

**Problema completo**: https://www.urionlinejudge.com.br/judge/pt/problems/view/1159

# Resolução

Primeiramente, iremos declarar nossas variáveis. `X`, `soma` o resultado da soma dos 5 pares consecutivos a partir de X, inclusive o X , se for par e por fim, `i` o contador do loop `for` que virá a seguir.

```c
    int X, i, soma;
``` 

Tendo a variável declarada, podemos receber o número X utilizando a função `scanf` e o `%d` para se referir ao inteiro `X`. Precisamos receber a variável antes de entrar no loop para a condição ser respeitada e o loop iniciar, ou no caso do valor recebido já ser nossa condição de parada, encerrar o programa.

```c
    scanf("%d",&X);
```

Como não temos o número de casos de teste que faremos e sim uma condição de parada, utilizaremos um loop `while` para fazer a mesma operação de soma até que o número informado em `X` seja 0. Podemos dividir esse processo em 3 etapas

1. Zeramos a variável `soma` para evitar que o resultado da operação anterior afete na atual.
2. Efetuamos o processo de soma.
3. Escrevemos o resultado na tela e recebemos o próximo valor de `X`.

```c
    while(X != 0){
        soma = 0;
        /*
            [Processo de soma]
        */
        printf("%d\n",soma);
        scanf("%d",&X);
    }
``` 

Focando no processo de soma agora, temos um loop `for` interno que faz uma contagem de 0 a 5 pois precisamos somar os 5 próximos números a partir de `X` que sejam pares. 

Para a verificação de paridade, utilizamos o condicional `if(X%2 == 0)`, ou seja, se `X` for par.

* Caso `X` seja par, somamos `X` na variável `soma` (`soma += X` é o mesmo que `soma = soma + X`) e pulamos para o próximo par (`X += 2`)  
* Caso `X` seja impar (`else`), somamos `X`+1 na variável `soma`, ou seja, o próximo par, e então pulamos para o próximo impar, pra sempre cair no `else`
 
```c
    ...
    for(i=0;i<5;i++){
            if(X%2 == 0){
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

Dessa forma, somaremos apenas os números pares e armazenamos na variável `soma`, que escrevemos na tela ao fim do `for` interno com a função `printf`, assim, podemos reutilizá-la zerando-a na próxima iteração do loop.

```c
     while(X != 0){
        soma = 0;
        for(i=0;i<5;i++){
            if(X%2 == 0){
                soma += X;
                X+=2;
            }
            else{
                soma += X + 1;
                X += 2;
            }
        }
        printf("%d\n",soma);
        scanf("%d",&X);
    }
```

Ao escrever o valor da variável `soma` na tela, também recebemos o próximo valor de `X` e recomeçamos o processo, passando pela verificação se chegamos à nossa condição de parada (`X == 0`) verificada pelo trecho `while(X != 0)`.

Caso tenha alguma dúvida sobre este problema ou sobre a resolução, entre em contato com o PET-BCC pelo nosso
[Facebook](https://www.facebook.com/petbcc/),
[Instagram](https://www.instagram.com/petbcc.ufscar/)
ou nos mande um e-mail com o assunto "URI" para  petbcc.ufscar@gmail.com
