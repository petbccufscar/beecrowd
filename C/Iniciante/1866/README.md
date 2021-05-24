# Problema:
Dois amigos pedem ao atendente de uma lanchonete propor um desafio, de modo que quem acertasse mais, não precisaria pagar a conta. Então foi proposto o seguinte: Dado o seguinte somatório abaixo, informar o resultado, com uma quantidade de termos no mesmo:

S = 1 - 1 + 1 - 1 + 1 - 1 + 1 - 1 ...

Escreva um programa que, dada uma quantidade de termos, informar o resultado do somatório acima.

##### Link do problema: https://www.urionlinejudge.com.br/judge/pt/problems/view/1866
 
# Resolução:

O exercício consiste de uma série de somas e subtrações de *1*, o primeiro sempre será *+1*, a partir daí intercalando somatório e subtração; como nós só iremos receber o número de termos podemos descobrir a soma com ele, se ele for par a soma é *0*, senão é *1*.

Primeiro instanciamos as variáveis necessárias, sendo elas: 3 inteiros (`C` para o número de casos de teste; `contagem` para contar o loop; e `N` para o numero de termos).
Começamos lendo o número de casos de teste.

```c
    int C, N, contagem = 0;

    scanf("%d", &C);
```
 
Agora iremos utilizar um `while()` para passar por todos os casos de teste, incrementando a contagem ao final do `while()` até alcançar `C`. Dentro dele iremos ler `N`. Após ler iremos utilizar um `if()` para verificar se a soma será 1 ou 0, para isso utilizaremos o resto de uma divisão inteira por 2 (`%2`), sendo que se o resto for 0 iremos imprimir `0`, caso contrário (`else`) imprimimos `1`.

```c
    while (contagem < C) {
        scanf("%d", &N);

        if (N % 2 == 0) printf("0\n");
        else printf("1\n");

        contagem++;
    }
```

##### Para aprender um pouco mais sobre o laço de repetição while: [While](http://linguagemc.com.br/o-comando-while-em-c/)
 
Caso tenha alguma dúvida sobre este problema ou sobre a resolução, entre em contato com o PET-BCC pelo nosso
[Facebook](https://www.facebook.com/petbcc/),
[Instagram](https://www.instagram.com/petbcc.ufscar/)
ou nos mande um e-mail com o assunto "URI" para  petbcc.ufscar@gmail.com