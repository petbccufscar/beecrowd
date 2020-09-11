# Problema:
Neste problema o seu trabalho é verificar se um conjunto de processos periódicos que possuem restrição de tempo-real pode ser escalonado.

Um processo de tempo real é caracterizado por dois números. O primeiro é o custo computacional do processo. Ou seja, o tempo que o processo gasta quando entrar em execução. O segundo número é o período em que o processo executa. Ou seja, a cada período de tempo, o processo reinicia.

O conjunto será escalonado usando o algoritmo EDF (Earliest Deadline First). Sabe-se que o algoritmo EDF é ótimo. Ou seja, se um conjunto de tarefas não poder ser escalonado pelo EDF, ele não poderá ser escalonado por nenhum outro algoritmo.

O sistema operacional que receberá estas tarefas está rodando em uma máquina single core. As tarefas são preemptáveis. Isto é uma tarefa pode tomar o lugar de outra durante a execução, se for necessário.

Considere que o custo de trocar entre tarefas é 0.

**Problema Completo**: https://www.urionlinejudge.com.br/judge/pt/problems/view/2823


# Resolução:
Para resolvermos este exercício, não é preciso implementar toda a lógica do algoritmo preemptivo "Earliest Deadline First", resultando em um escalonamento completo. Basta realizarmos a análise dos valores fornecidos, aplicando nestes o [teste de escalonabilidade](https://www.cin.ufpe.br/~if728/sistemas_tempo_real/livro_farines/cap2.pdf).  

Iniciamos com a declaração das variáveis inteiras `N` (quantidade de processos) e `i` (iterações do loop); bem como a variável `soma`, do tipo `long double`, que armazenará o somatório obtido na análise. Em seguida, realizamos a leitura do número de processos através da função `scanf` e, tendo este valor em mãos, podemos utilizá-lo para determinar o tamanho dos vetores inteiros `custo` e `periodo`, em que cada posição destes corresponde a um processo diferente.  

```c
int N, i;
long double soma=0;

scanf("%d",&N);

int custo[N], periodo[N];
```  

A estrutura de repetição `for` conterá `N` iterações para que, em cada uma, realize-se a leitura do custo computacional e período dos processos, dispondo tais dados nos vetores apropriados; além da atualização de `soma`, incrementando a esta a razão entre os valores do processo atual recém armazenado.  

```c
for(i=0; i<N; i++){
  scanf("%d %d",&custo[i],&periodo[i]);
  soma = soma + ( (float)custo[i] / (float)periodo[i] );
}
```  

Ao final do loop, verificamos o valor de `soma`. Se este for menor ou igual a 1, `if` garante que o comando `printf` imprima "OK" na tela. Caso contrário, `else` conterá a exibição de "FAIL".  

```c
if(soma <= 1)
  printf("OK\n");

else
  printf("FAIL\n");
```


##### Para aprender um pouco mais sobre tipos de dados: [Tipos de dados](https://pt.wikibooks.org/wiki/Programar_em_C/Tipos_de_dados)

Caso tenha alguma dúvida sobre este problema ou sobre a resolução, entre em contato com o PET-BCC pelo nosso [Facebook](https://www.facebook.com/petbcc/), [Instagram](https://www.instagram.com/petbcc.ufscar/) ou nos mande um e-mail com o assunto "URI" para  petbcc.ufscar@gmail.com
