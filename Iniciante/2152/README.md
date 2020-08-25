# Problema:
Um dia, o grande herói Chapolout foi ajudar um cientista, que criou muitas invenções. Uma destas invenções é um sistema que abre a porta secreta do laboratório. O sistema consiste em retirar uma vela do candelabro do lado da porta, que a mesma se abre, e, ao colocar a vela de volta ao candelabro, a porta se fecha. Porém, Chapolout descobriu que a vela era só uma desculpa. Na verdade, o assistente do cientista, chamado Pepe, é que abria a porta do laboratório, por dentro. Um tempo depois, o sistema foi modificado, para funcionar igualmente ao projeto inicial. Colocaram um sensor de pressão embaixo da vela do candelabro, de modo que a retirada da vela ativa o sistema. Este sistema emite um relatório de log por cada vez que a porta abriu ou fechou, mas o log está bem confuso. A cada registro, três números inteiros são cadastrados, sendo a hora e o minuto que o evento ocorreu e um valor que representa se a porta abriu ou fechou naquele momento. Pepe pede a sua ajuda para converter os dados do log em dados mais legíveis para ele.

Escreva um programa que, dado um registro de log, este seja convertido em textos mais legíveis.
 
 
##### Link do problema: https://www.urionlinejudge.com.br/judge/pt/problems/view/2152
 
 
# Resolução:
 
Para imprimir a ocorrência de forma mais legível, iremos declarar quatro variáveis do tipo `inteiro`,  `numTestes`, `hora`, `minuto` e `abriu`. A variável `abriu` indica a própria ocorrência (zero se a porta fechou ou um se a porta abriu).
 
```c
int numTestes, hora, minuto, abriu;
```

Em seguida, lemos o número de casos testes.

```c
scanf("%d", &numTestes);
```

Em seguida, vamos utilizar a estrutura de repetição `while(numTestes)` para o programa funcionar até que o valor de `numTestes` seja 0, já que todo valor positivo é interpretado como verdadeiro.

A cada iteração do laço de repetição:
- lemos `hora`, `minuto` e `abriu` ;
- exibimos `hora` e `minuto`, com dois dígitos, sem quebra de linha e no formato pedido;
- Verificamos se `abriu` é um ou zero:
    -caso seja um, exibimos `abriu!` com quebra de linha
    -caso seja zero, exibimos `fechou!` com quebra de linha
- diminuímos em 1 `numTestes`.

```c
while(numTestes){

    scanf("%d %d %d", &hora, &minuto, &abriu);
    printf("%02d:%02d - A porta ", hora, minuto);
       
    if(abriu)
        printf("abriu!\n");
    else
        printf("fechou!\n");

    numTestes--;
}
```
 
 
Caso tenha alguma dúvida sobre este problema ou sobre a resolução, entre em contato com o PET-BCC pelo nosso
[Facebook](https://www.facebook.com/petbcc/),
[Instagram](https://www.instagram.com/petbcc.ufscar/)
ou nos mande um e-mail com o assunto "URI" para  petbcc.ufscar@gmail.com