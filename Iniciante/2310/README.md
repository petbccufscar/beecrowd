# Problema:
Um treinador de voleibol gostaria de manter estatísticas sobre sua equipe. A cada jogo, seu auxiliar anota quantas tentativas de saques, bloqueios e ataques cada um de seus jogadores fez, bem como quantos desses saques, bloqueios e ataques tiveram sucesso (resultaram em pontos). Seu programa deve mostrar qual o percentual de saques, bloqueios e ataques do time todo tiveram sucesso.
 
##### Link do problema: https://www.urionlinejudge.com.br/judge/pt/problems/view/2310
 
# Resolução:
O exercício consiste em ler o nome dos jogadores e suas respectivas estatísticas, e com elas imprimir a porcentagem de sucesso em cada categoria.

Primeiro instanciamos as variáveis necessárias, sendo elas: 8 inteiros (`N` o número de participantes, `S` saques, `B` bloqueios, `A` ataques, `S1` saques bem sucedidos, `B1` bloqueios bem sucedidos, `A1` ataques bem sucedidos e `contagem` para contar o número de jogadores lidos pelo `for()` que iremos utilizar), 9 `double` (para armazenar as somas dos `S`, `B`, `A`, `S1`, `B1` e `A1` e seus respectivos resultados, que será da equipe) e um vetor de `char`(para armazenar o nome dos jogadores).
Começamos lendo o número de jogadores.

```c
    int N, S, B, A, S1, B1, A1, contagem;
    double soma_S, soma_B, soma_A;
    double soma_S1, soma_B1, soma_A1;
    double resultado_S, resultado_B, resultado_A;
    char name[20];
    scanf("%d", &N);
```
 
Agora iremos utilizar um `for()` para passar por todos os jogadores. Dentro dele iremos ler todos os valores do jogador referente, sendo eles: `nome`, `S`, `B`, `A`, `S1`, `B1` e `A1`, respectivamente nessa ordem. Após ler todos iremos adicionar os valores às somas respectivas, para calcular o resultado da equipe futuramente.

Obs: Como vamos ler um vetor completo de `char`, iremos ler utilizando `%s`.

```c
    for (contagem = 1; contagem <= N; contagem++)
    {
        scanf("%s", nome);
        scanf("%d%d%d", &S, &B, &A);
        scanf("%d%d%d", &S1, &B1, &A1);
        soma_S += S;
        soma_B += B;
        soma_A += A;
        soma_S1 += S1;
        soma_B1 += B1;
        soma_A1 += A1;
    }
```

Tendo lido todos os valores de todos os jogadores iremos calcular a porcentagem de sucesso de cada tipo de tentativa (saque, bloqueio e ataque), para isso iremos dividir o número de sucessos pelo número de tentativas e multiplicá-lo por 100 para obter a porcentagem.

```c
    resultado_S = (soma_S1 / soma_S) * 100.00;
    resultado_B = (soma_B1 / soma_B) * 100.00;
    resultado_A = (soma_A1 / soma_A) * 100.00;
```

Por fim imprimimos os resultados de cada tipo de tentativa.

```c
    printf("Pontos de Saque: %.2lf %%.\n", resultado_S);
    printf("Pontos de Bloqueio: %.2lf %%.\n", resultado_B);
    printf("Pontos de Ataque: %.2lf %%.\n", resultado_A);
```

Obs: Precisamos imprimir com 2 casas decimais um tipo `double`, sendo assim, teremos que especificar isso, `.2` para o número de casas decimais, `l` pois é um `double` e `f` pois é preciso ser `float` para poder utilizar casas decimais. Para imprimir o símbolo de porcentagem utilizamos dois deles `%%`.

 
Caso tenha alguma dúvida sobre este problema ou sobre a resolução, entre em contato com o PET-BCC pelo nosso
[Facebook](https://www.facebook.com/petbcc/),
[Instagram](https://www.instagram.com/petbcc.ufscar/)
ou nos mande um e-mail com o assunto "URI" para  petbcc.ufscar@gmail.com

