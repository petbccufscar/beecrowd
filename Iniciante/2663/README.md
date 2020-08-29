# Problema:

Em diversas competições acadêmicas, como a Olimpíada Brasileira de Informática (OBI), uma certa quantidade de competidores se classifica de uma fase para a fase seguinte, garantindo uma das vagas disponíveis. Entretanto, normalmente essa quantidade é variável, pois dada uma certa quantidade mínima de classificados, é frequente que haja empate na última vaga de classificação. Neste caso, é comum que todos os competidores empatados na última colocação se classifiquem.

Sua tarefa é ajudar a calcular o número de competidores classificados para a próxima fase. Você receberá uma lista de pontuações obtidas pelos competidores e o número mínimo de vagas para a fase seguinte e você deve decidir quantos competidores de fato vão se classificar.

Exemplo de Entrada:

                        10
                        3
                        1
                        2
                        3
                        4
                        5
                        5
                        4
                        3
                        2
                        1

Saída: 

                        4


###### Problema completo: https://www.urionlinejudge.com.br/judge/pt/problems/view/2663

# Resolução

A questão do exercício é dado o número de questões e o número mínimo de classificados, definir a quantidade de pessoas que iram passar usando como critério a nota feita em cada exercício. 

Começamos declarando e lendo algumas variáveis:

```c
        int N, i, j, pivo, classificados;
        scanf("%d", &N);
        int Participantes[N];
        
        int NumPassou;
        scanf("%d", &NumPassou);
        int Passou[NumPassou], cont=0;
```

`N` é a variável que representa o número de participantes, `i, j` variáveis de iteração, `pivo` usado mais a frente para ajudar na troca de valores. Fazemos um `scanf` do `N` antes de declarar um vetor, devido a esse `N` ser o tamanho dele, `Participantes[N]` vetor que armazena a nota das questões dos participantes. `NumPassou` é a variável referente quantidade mínima de participantes, lemos ela no `scanf` pelo mesmo motivo de `N`, declaramos o vetor `Passou[NumPassou]` que representa o número total efetivo de candidatos que passaram e `cont` que servirá mais pra frente como um contador.

Seguimos para a leitura das notas de cada um dos `N` participantes:

```c
        for (i = 0; i < N; i++)
        {
                scanf("%d", &Participantes[i]);
        }
```

Uma estratégia para se resolver o exercício é ordenar o vetor das notas `Participantes[]` para facilitar depois a verificação das maiores notas e definir os que iram passar.

```c
        i = 1;
        while (i < N)
	{
		j = i - 1;
		pivo = Participantes[i];

		while (j >= 0 && Participantes[j] < pivo)
		{

			Participantes[j + 1] = Participantes[j];
			j--;

		}

		Participantes[j + 1] = pivo;
		i++;
	}
```
Iniciamos setando o `i=1` para podermos iniciar a comparação e assim comparar a primeira posição `[0]` com a segunda `[1]`, `j` receberá a primeira posição na primeira iteração e nas seguintes ele recebera a posição anterior `j = i-1`. `pivo` irá receber o valor da posição seguinte do vetor `Participantes[]`. Dentro do `while` o menor valor está sendo jogado para o final do vetor e ao sair é passado o maior valor para a posição anterior da que foi verificada dentro do `while`, fazendo com que os maiores números permaneçam no inicio do vetor, `i++` para seguir a comparação de todas as posições.    

Setamos valores para `j` e `i` para podermos usar no `while` que irá fazer a verificação se há mais participantes classificados do que nos foi passado `NumPassou`(número mínimo de participantes), `classificados` é o nosso contador que será incrementado caso a situação explicada seja verdade, por isso ele de inicio tem que receber o valor mínimo de participantes `NumPassou`.

```c
        j=NumPassou;
        i=NumPassou - 1;
        classificados=NumPassou;
```

Lembrando que tendo como número mínimo de participantes passados `NumPassou` e o vetor `Participantes[]` podemos tirar dai que as primeira posições do nosso vetor são os candidatos que já eram esperados passar e por isso iniciamos verificando se a posição seguinte a esse número já esperado é igual a anterior (última posição dos esperados para se classificar), e caso for classificados é incrementado.

```c
        while (Participantes[j++] == Participantes[i])
        {
                classificados++;                                         
        }
```

Finalizamos printando a saída pedida pelo Uri:

```c
       printf("%d\n", classificados);
```

Caso tenha alguma dúvida sobre este problema ou sobre a resolução, entre em contato com o PET-BCC pelo nosso
[Facebook](https://www.facebook.com/petbcc/),
[Instagram](https://www.instagram.com/petbcc.ufscar/)
ou nos mande um e-mail com o assunto "URI" para petbcc.ufscar@gmail.com