# Problema:

Googlbook é uma famosa empresa de TI que abriu um escritório em sua cidade este ano! Além disso, Googlbook acaba de oferecer entrevistas para um cargo de estágio na empresa!

Para ser entrevistado, você precisa enviar alguns dados pessoais para a empresa, que serão usados para decidir quem ficará com o cargo. Você enviou todas as informações de que eles precisam, exceto uma: seu API (Índice de Desempenho Acadêmico). Para piorar as coisas, o Portal do Aluno, o sistema que fornece sua API, não está funcionando!

Felizmente, você se lembra de todas as notas que obteve em todas as disciplinas **M** que cursou, bem como de suas cargas horárias. Você também se lembra de como a API é calculada:

![Fórmula](https://resources.urionlinejudge.com.br/gallery/images/novos/estagio_fig.png)

, onde **N<sub>1<sub>**, **N<sub>2<sub>**, ..., **N<sub>M<sub>** são suas notas em cada disciplina e **C<sub>1<sub>**, **C<sub>2<sub>**, ..., **C<sub>M<sub>** são a carga horária das respectivas disciplinas.

De acordo com as notas que você obteve e a carga de trabalho de cada disciplina, determine sua API, para que você possa enviá-la ao Googlbook o mais rápido possível!

**Problema Completo:** https://www.urionlinejudge.com.br/judge/en/problems/view/2533

# Resolução:

Para resolver o problema, será necessário informar o número `M` de disciplinas cursadas, onde `M` deve estar dentro do intervalo de 1 a 40 (1 =< M =< 40). Ademais, para cada disciplina, será lido dois valores por linha, a nota `N` e a carga horária `C`.

Primeiro declaramos as variáveis `M`, `N` e `C`, do tipo inteiro (onde `N` e `C` são vetores), que receberão o número de disciplinas, as notas e as cargas horárias, respectivamente. Também, será necessário adicionar a variavel `i` do tipo inteiro que servirá como um contador, e as variaveis `resultado`, `cima` e `baixo` do tipo double que serão utilizadas na hora do cálculo.

```c
int M, N[40], C[40], i;
double resultado, cima, baixo;
```

Depois, iniciamos o laço de repetição `while`, onde a condição de parada do laço possui o comando `scanf`, que fará a leitura da variável `M` até que receba o [final de arquivo (EOF)](https://pt.wikipedia.org/wiki/EOF), encerrando o laço de repetição.

```c
while (scanf("%d",&M) != EOF ) {
	/*
		restante do código omitido
	*/
} 
```

Agora, dentro do `while` começamos a escrever o nosso código, no qual será lido os valores das notas e das cargas horarias e armazenados nos vetores `N` e `C` , através do seguinte laço de repetição `for`. Para um determinado número M de disciplinas, serão lidos N(M) notas e C(M) cargas horarias.

```c
while (scanf("%d",&M) != EOF ) {	
    for ( i=0; i<M; i++ ) {
        scanf("%d %d", &N[i], &C[i]);
    }
}
```

Com isso, ainda dentro do loop `while` definimos os valores que queremos calcular como 0, para não influenciar as operações dentro do proximo passo.

```c
resultado = 0;
cima = 0;
baixo = 0;
```

Agora, com todos os valores em mãos, ainda dentro do `while` iremos calcular os somatórios para obter o numerador e denominador da divisão.
Para isto, fazemos dois laços de repetição `for`, para calcularmos, primeiramente o somatório superior da divisão (numerador), sendo este o somatório das (notas * carga horaria) que é armazenado na variável `cima`; Posteriormente, o somatório inferior da divisão (denominador), sendo este o somatório (carga horaria * 100) que é armazenado na variável `baixo`.
E por fim, obtemos o `resultado` fazendo a divisão do resultado dos dois somatórios (como proposto na fórmula):

```c
for ( i=0; i<M; i++ ) {
    cima = cima + ( N[i]*C[i] ) ;
}
for ( i=0; i<M; i++ ) {
    baixo = baixo + ( C[i] * 100) ;
}
resultado = cima / baixo;

```

Desta forma, basta escrever o resultado final no código utilizando o comando `printf`:
```c
printf("%.4lf\n",resultado);
```

##### Para aprender um pouco mais sobre final de arquivo (EOF): [EOF](https://pt.wikipedia.org/wiki/EOF)

##### Para aprender um pouco mais sobre operadores lógicos: [Operadores Lógicos](http://linguagemc.com.br/operadores-logicos-em-c/)

Caso tenha alguma dúvida sobre este problema ou sobre a resolução, entre em contato com o PET-BCC pelo nosso
* [Facebook](https://www.facebook.com/petbcc/)
* [Instagram](https://www.instagram.com/petbcc.ufscar/)
* ou nos mande um e-mail com o assunto "URI" para  petbcc.ufscar@gmail.com
