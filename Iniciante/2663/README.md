# Problema:

Em diversas competições acadêmicas, como a Olimpíada Brasileira de Informática (OBI), uma certa quantidade de competidores se classifica de uma fase para a fase seguinte, garantindo uma das vagas disponíveis. Entretanto, normalmente essa quantidade é variável, pois dada uma certa quantidade mínima de classificados, é frequente que haja empate na última vaga de classificação. Neste caso, é comum que todos os competidores empatados na última colocação se classifiquem.

Sua tarefa é ajudar a calcular o número de competidores classificados para a próxima fase. Você receberá uma lista de pontuações obtidas pelos competidores e o número mínimo de vagas para a fase seguinte e você deve decidir quantos competidores de fato vão se classificar.


###### Problema completo: https://www.urionlinejudge.com.br/judge/pt/problems/view/2663

# Resolução

O problema do exercício é: dado o número de questões e o número mínimo de classificados, definir a quantidade de pessoas que irão passar de acordo com sua nota, considerando que podem haver notas empatadas na última posição.

Começamos declarando e lendo algumas variáveis:

```c
        int N, i, j, pivo, minclassificados;
        scanf("%d", &N);
        int Participantes[N];
        
        int numpassou;
        scanf("%d", &numpassou);
        
```

`N` é a variável que representa o número de participantes, `i, j` variáveis de iteração, `pivo` usado mais a frente para ajudar na troca de valores. Fazemos um `scanf` do `N` antes de declarar um vetor, devido a esse `N` ser o tamanho dele, `Participantes[N]` vetor que armazena a nota das questões dos participantes. `numpassou` é a variável referente quantidade mínima de participantes, lemos ela no `scanf` pelo mesmo motivo de `N`.

Seguimos para a leitura da nota de cada um dos `N` participantes:

```c
        for (i = 0; i < N; i++)
        {
                scanf("%d", &Participantes[i]);
        }
```

Uma estratégia para se resolver o exercício é ordenar o vetor `Participantes[]`, que contém as notas, e definir quantos irão passar baseado na nota do último aprovado.

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

Iniciamos os valores para `j` e `i` para podermos usar no `while` que irá fazer a verificação se há mais participantes classificados do que nos foi passado `numpassou`(número mínimo de participantes), `minclassificados` é o nosso contador que será incrementado caso a situação explicada seja verdade, por isso ele de inicio tem que receber o valor mínimo de participantes `numpassou`.

```c
        j=numpassou;
        i=numpassou - 1;
        minclassificados=numpassou;
```

Como  sabemos o número mínimo de participantes aprovados `NumPassou` e temos o vetor de notas  `Participantes[]` ordenado, podemos concluir que as primeira posições do vetor são os primeiros candidatos aprovados. A partir da nota do último classificado, que está em `Participantes[j]`, vamos verificar quantos participantes tiraram a mesma nota e também devem ser aprovados. Nesse caso, incrementamos a variável `classificados` além do número mínimo.

```c
        while (Participantes[j++] == Participantes[i])
        {
                minclassificados++;                                         
        }
```

Finalizamos exibindo a saída pedida pelo URI:

```c
       printf("%d\n", minclassificados);
```
#### Para aprender um pouco mais sobre: [Estrutura de repetição for](http://linguagemc.com.br/a-estrutura-de-repeticao-for-em-c/)

#### Para aprender um pouco mais sobre: [Métodos de Ordenações](https://www.treinaweb.com.br/blog/conheca-os-principais-algoritmos-de-ordenacao/)

Caso tenha alguma dúvida sobre este problema ou sobre a resolução, entre em contato com o PET-BCC pelo nosso
[Facebook](https://www.facebook.com/petbcc/),
[Instagram](https://www.instagram.com/petbcc.ufscar/)
ou nos mande um e-mail com o assunto "URI" para petbcc.ufscar@gmail.com