# Problema

Chegamos finalmente no final do semestre e pra variar, trabalhos estão acumulados! Os professores, com a intenção de ajudar (ou não), decidiram que os trabalhos será feitos em duplas, além disso, eles dariam o spoiler do grau de dificuldade que um trabalho tem para ser feito.

###### Problema completo: https://www.urionlinejudge.com.br/judge/pt/problems/view/2715

# Resolução

Para resolver o problema, iremos receber o grau de dificuldade dos trabalhos e salvá-los em um vetor. Em seguida, iremos manter uma variável na posição final e uma na posição inicial do vetor, para realizar a separação dos trabalhos.

Começamos inicializando as variáveis. Todas serão do tipo `long long int`, devido à natureza dos valores do exercício serem muito grandes.
Serão elas:
* `N`, o número de trabalhos para a divisão;
* `X[]`, o vetor que armazenará o grau de dificuldade de cada trabalho;
* `somaGugu`, a soma das dificuldades dos trabalhos que Gugu fará;
* `somaRangel`, a soma das dificildades dos trabalhos para Rangel;
* `i`, a variável que iterará no começo do vetor;
* `j`, a variável para o fim do vetor.
```c
	long long int N, X[1000000], somaGugu, somaRangel, i, j;
```

Iniciamos nossa estrutura de repetição `while`, que irá receber e processar as entradas enquanto `N` não seja `EOF`.
```c
	while(scanf("%lld", &N) != EOF){
```

Em seguida, utilizaremos a estrutura `for` para receber os graus de dificuldade dos trabalhos e armazenar em cada posição do vetor `X`.
```c
	for(i = 0; i < N; i++)
		scanf("%lld", &X[i]);
```

Inicializamos nossas variáveis de iteração `i` e `j` para a primeira e a última posição do vetor, respectivamente, e as somas de cada amigo como 0, visto que nenhum trabalho foi designado ainda.
```c
	i = 0;
	j = N-1;
	somaGugu = 0;
	somaRangel = 0;
```

Enquanto a variável de início for igual ou menor do que a variável de fim, a estrutura de repetição `while` continua no loop.
```c
	while(i<=j){
```

Caso a soma de trabalhos do Rangel com o i-ésimo trabalho da fila seja menor ou igual à soma de trabalhos do Gugu com o j-ésimo trabalho, o trabalho vai para Rangel e a variável de posição inicial soma em 1, visto que um dos primeiros trabalhos já foi atribuído para Rangel.
```c
	if((somaRangel + X[i]) <= (somaGugu + X[j])){

		somaRangel += X[i];
		i++;
	}
```

Caso contrário, adicionamos o trabalho para Gugu e diminuimos a variável de final, visto que um trabalho já foi atribuido e pode parar de ser considerado para o vetor.
```c
	else{
		somaGugu += X[j];
		j--;
```

Por fim, exibimos a diferença entre as atribuições com o `printf`, de forma que a diferença não seja negativa. Desta forma, verificamos qual das duas somas é maior e mostramos a diferença entre elas.
```c
	if(somaRangel >= somaGugu)
		printf("%lld\n", somaRangel - somaGugu);

	else
		printf("%lld\n", somaGugu - somaRangel);
```

Caso tenha alguma dúvida sobre este problema ou sobre a resolução, entre em contato com o PET-BCC pelo nosso
[Facebook](https://www.facebook.com/petbcc/),
[Instagram](https://www.instagram.com/petbcc.ufscar/)
ou nos mande um e-mail com o assunto "URI" para  petbcc.ufscar@gmail.com
