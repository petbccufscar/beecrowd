# Problema:
Em uma determinada competição de saltos ornamentais, cada salto recebe um grau de dificuldade e é avaliado por sete juízes. Após cada salto, os juízes, que não se comunicam uns com os outros, mostram suas notas. Um salto é cotado entre zero e dez pontos. Depois de apresentadas as notas, a mais alta e a mais baixa são descartadas. O restante é somado e multiplicado pelo grau de dificuldade do salto, que gira entre 1,2 e 3,8, definido sempre antes do início da apresentação do atleta. O julgamento então é feito da seguinte forma: supondo que um saltador tenha sua nota de partida (seu grau de dificuldade de movimento) avaliada em 2,0 e tire notas 6,0, 5,0, 5,0, 5,0, 5,0, 5,0, 4,0 em sua execução. Disso, retira-se a nota mais baixa e a mais alta, o que gera um resultado parcial de 25,0. Então, pega-se a nota de execução e multiplica-a pela nota de partida para se chegar ao resultado final, que neste exemplo é de 50,0. Seu programa deve apresentar o resultado de uma competição de acordo com estas regras.
 
##### Link do problema: https://www.urionlinejudge.com.br/judge/pt/problems/view/2311
 
# Resolução:
O exercício consiste em sua ler o número de competidores; ler o grau de dificuldade, nome e notas do respectivo participante; e mostrar a nota de cada um competidor.

Primeiro instanciamos as variáveis necessárias, sendo elas: 3 inteiros (`N` para o número de competidores e `i` e `j` para controla os 2 `for()` aninhados que iremos utilizar); 25 `double` (`GD` para o grau de dificuldade, `pontuacao`, `max` para a pontuação máxima, `min` para a pontuação mínima e a `soma` para somar todas as pontuações de um competidor); e um vetor de `char` (para o `nome`).
Começamos lendo o número de competidores.

```c
    int N, i, j;
    char nome[20];
    double GD, pontuacao, max = 0.00, min = 10.00, soma = 0.00;
    scanf("%d", &N);
```
 
Agora iremos utilizar um `for()` para passar por todos os competidores, sempre resetando as pontuações (`max = 0.00`, `min = 10.00`, `soma = 0.00`) ao final de cada loop. Antes de lermos as pontuações iremos ler o `nome` e o `GD` do competidor.

Agora iremos utilizar outro `for()` dentro desse para ler as 7 pontuações, a cada leitura iremos conferir se essa é a maior ou a menor já lida desse competidor e iremos armazenar em `max` ou `min` respectivamente e antes de fechar o `for()` somamos a `pontuacao` a soma.

Depois de ler as pontuações, retiramos `max` e `min` da soma, pois não serão consideradas, e multiplicamos pelo grau de dificuldade. Assim temos o resultado daquele competidor e já podemos imprimir seu `nome` e `resultado`.

```c
    for(i=1; i<=N; i++)
    {
        scanf("%s", nome);
        scanf("%lf", &GD);
        for(j=1; j<=7; j++)
        {
            scanf("%lf", &pontuacao);
            if(pontuacao > max) max = pontuacao;
            if(pontuacao < min) min = pontuacao;
            soma += pontuacao;
        }
        soma -= (max+min);
        soma *= GD;
        printf("%s %.2lf\n", nome, soma);
        max = 0.00, min = 10.00, soma = 0.00;
    }
```

##### Para aprender um pouco mais sobre estrutura de seleção: [If/Else](https://www.inf.pucrs.br/~flash/cbp/selecao_if.html)
 
Caso tenha alguma dúvida sobre este problema ou sobre a resolução, entre em contato com o PET-BCC pelo nosso
[Facebook](https://www.facebook.com/petbcc/),
[Instagram](https://www.instagram.com/petbcc.ufscar/)
ou nos mande um e-mail com o assunto "URI" para  petbcc.ufscar@gmail.com

