# Problema:
Odin criou para Thor a mais fiel e poderosa arma possível, o martelo Mjölnir. Feito de um minério místico especial chamado Uru e forjado no coração de uma estrela pelos Deuses ferreiros de Asgard, Brokk e Eitri, os lendários ferreiros.

Um dia, Thor desafiou seus amigos para ver quem conseguia levantar o Mjölnir.

Escreva um programa que, dado um nome, e a força, em Newtons, aplicado ao tentar levantar o Mjölnir, informar se a pessoa conseguiu ou não levantá-lo.
 
##### Link do problema: https://www.urionlinejudge.com.br/judge/pt/problems/view/1865
 
 
# Resolução:
 
Primeiro instanciámos as variáveis necessárias, sendo elas: 3 inteiros (`C` para o numero de casos de teste; `contagem` para contar o loop; e `newtons` para ler a força) e um char com 10 espaços (`nome[10]`).
Começamos lendo o número de casos de teste.

```c
    int C, contagem, newtons;
    char nome[10];
    scanf("%d", &C);
```

 Agora iremos utilizar um `for()` para passar por todos os casos de teste. Dentro dele iremos ler cada `nome` e `newtons` referentes. Após ler iremos utilizar um `if()` para verificar se o herói e digno ou nao, assim gerando as saídas `Y` e `N` respectivamente.
 Obs: Iremos utilizar `%s` para ler toda a `string` que foi passada e como `nome` é tratado como um ponteiro diretamente não é necessário o `&` para fazer sua referencia.

```c
    for (contagem=1; contagem<=C; contagem++)
    {
        scanf("%s", nome);
        scanf("%d", &newtons);
        if (nome[0]=='T' && nome[1]=='h' && nome[2]=='o' && nome[3]=='r')
            printf("Y\n");
        else printf("N\n");
    }
```

##### Para aprender um pouco mais sobre o laço de repetição for: [For](http://linguagemc.com.br/a-estrutura-de-repeticao-for-em-c/)
 
##### Para aprender um pouco mais sobre matriz: [Matriz](http://linguagemc.com.br/matriz-em-c/)
 
Caso tenha alguma dúvida sobre este problema ou sobre a resolução, entre em contato com o PET-BCC pelo nosso
[Facebook](https://www.facebook.com/petbcc/),
[Instagram](https://www.instagram.com/petbcc.ufscar/)
ou nos mande um e-mail com o assunto "URI" para  petbcc.ufscar@gmail.com