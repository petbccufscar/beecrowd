# Problema:
Esse ano as Renas do papai Noel decidiram que Rudolph não seria mais aquele que sempre ficaria à frente. Elas escolheriam de forma justa entre elas quem iria encabeçar o trenó. E nada é mais justo que o acaso.

Então optaram pela seguinte forma para escolher: Cada Rena faria a quantidade que quisesse de bolas de neve, sem as outras verem. Depois, todas as bolas de neve de todas as Renas seriam reunidas em uma única e grande pilha. Por último, as bolas de neve seriam tiradas dessa pilha, uma a uma, e distribuídas entre elas sempre seguindo a ordem: Dasher, Dancer, Prancer, Vixen, Comet, Cupid, Donner, Blitzen e Rudolph. Até que se acabassem as bolas de neve. A rena que ficasse com a última bola de neve seria declarada vencedora e ficaria na posição principal do trenó este ano.

Dado o número de bolas de neve feitas por cada Rena, determine qual Rena ganhou o sorteio.

##### Link do problema: https://www.urionlinejudge.com.br/judge/pt/problems/view/2721
 
# Resolução:

O exercício consiste em ler as 9 quantidades de bolinhas e imprimir a última rena a pegar a bolinha.

Primeiro definimos os nomes das `renas` na respectiva ordem.  
Agora instanciamos as variáveis necessárias, sendo elas: 3 `int` (`i` para o `for()` que será utilizado; `A` para ler o número de bolinhas; e `soma` para a soma dos valores).

```c
    char *renas[] = {"Rudolph","Dasher", "Dancer", "Prancer", "Vixen", "Comet", "Cupid", "Donner", "Blitzen"};
    int i, A, soma = 0;
```

Para ler os 9 valores de bolinhas iremos utilizar um `for()` e, conforme vamos lendo, incrementamos o valor de `soma` com o valor lido.

```c
    for (i = 0; i < 9; i++)
    {
        scanf("%d", &A);
        soma += A;
    }
```

Agora nos resta imprimir a rena ganhadora com base no resto das bolinhas (`[soma % 9]`). Iremos utilizar o operador `%` para pegar o resta da divisão; que nesse caso será um valor inteiro de 0 a 8, que são os valores possíveis; de forma resumida é o valor que sobra e é menor que o divisor e que se nao fosse uma divisão inteira seria referente ao valor decimal menor que 1 do resultado. Como será um valor de 0 a 8 ele será usado como índice para selecionar o nome da rena vencedora no vetor de char `*renas[]`.

```c
    printf("%s\n", renas[soma % 9]);
```

##### Para aprender um pouco mais sobre a estrutura for: [For](http://linguagemc.com.br/a-estrutura-de-repeticao-for-em-c/)
##### Para aprender um pouco mais sobre o resto de divisão inteira: [Divisão](http://linguagemc.com.br/resto-de-uma-divisao-inteira-em-c/)

Caso tenha alguma dúvida sobre este problema ou sobre a resolução, entre em contato com o PET-BCC pelo nosso
[Facebook](https://www.facebook.com/petbcc/),
[Instagram](https://www.instagram.com/petbcc.ufscar/)
ou nos mande um e-mail com o assunto "URI" para  petbcc.ufscar@gmail.com
