# Problema:

As sequências de Iccanobif são sequências onde cada termo é sempre igual a soma dos dois próximos subsequentes a eles. Exceto pelos dois últimos termos os quais são sempre iguais a 1.

Exemplo de uma sequência de Iccanobif com 10 termos: 55, 34, 21, 13, 8, 5, 3, 2, 1, 1.

Sua tarefa é, dado um valor inteiro, imprimir a sequência de Iccanobif de tamanho correspondente.

###### Problema completo: https://www.urionlinejudge.com.br/judge/pt/problems/view/2807

# Resolução:

O objetivo deste problema é exibir a sequência de Fibonacci ao contrário (Iccanobif), a partir da quantidade total de itens recebida na entrada.

Para iniciar, declaramos as seguintes variáveis:
 * `N`, que será o tamanho da sequência de Iccanobif desejada;
 * `i`, que servirá para iterar sobre o laço de repetição;
 * `fibonacci`, que será um vetor de inteiros, utilizado para armazenar a sequência gerada e depois exibi-la ao contrário.
```c
int N, i; 
int fibonacci[40];
```

Realizamos a leitura de `N` (tamanho da sequência desejada) com o comando `scanf` e inicializamos as duas primeiras posições de `fibonacci` com 1 (padrão esclarecido pelo enunciado do exercício).
```c
scanf("%d", &N);
    
fibonacci[0]=1;
fibonacci[1]=1;
```

Em seguida, criamos um loop `for` para preencher o valor das próximas posições da sequência de Fibonacci. Este será iniciado com valor 2, pois as duas primeiras posições do vetor (`fibonacci[0]` e `fibonacci[1]`) já foram preenchidas; e continuará iterando até alcançar o valor de `N`. Para preenchermos os itens faltantes da sequência, somamos os valores contidos nas 2 posições anteriores a atual, visto que já inicializamos suas duas primeiras posições com 1.
```c
for(i=2; i<N; i++)
fibonacci[i] = fibonacci[i-1] + fibonacci[i-2];
```

Após o preenchimento do vetor de Fibonacci, devemos imprimi-lo ao contrário, com o objetivo de representá-lo de acordo com a sequência de Iccanobif. Isto é feito com um loop `for` iniciado com valor equivalente ao tamanho do vetor `fibonacci` (ou seja, `N-1`), decrementando até a posição `0`. Em seu escopo, exibimos cada posição da sequência com o comando `printf` e utilizamos uma estrutura `if-else` para que a saída seja no formato desejado pelo URI (último valor da sequência sem espaço e contendo `\n`).
```c
for(i = N-1; i>=0; i--){
	if(i>0)
		printf("%d ", fibonacci[i]);
	        
	else 
		printf("%d\n", fibonacci[i]);
}
```

##### Para aprender um pouco mais sobre o laço de repetição `for` : [for](http://linguagemc.com.br/a-estrutura-de-repeticao-for-em-c/)

Caso tenha alguma dúvida sobre este problema ou sobre a resolução, entre em contato com o PET-BCC pelo nosso
 * [Facebook](https://www.facebook.com/petbcc/),
 * [Instagram](https://www.instagram.com/petbcc.ufscar/)
 * ou nos mande um e-mail com o assunto "URI" para  petbcc.ufscar@gmail.com