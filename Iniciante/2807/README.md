# Problema:

As sequências de Iccanobif são sequências onde cada termo é sempre igual a soma dos dois próximos subsequentes a eles. Exceto pelos dois últimos termos os quais são sempre iguais a 1.

Exemplo de uma sequência de Iccanobif com 10 termos: 55, 34, 21, 13, 8, 5, 3, 2, 1, 1.

Sua tarefa é, dado um valor inteiro, imprimir a sequência de Iccanobif de tamanho correspondente.

###### Problema completo: https://www.urionlinejudge.com.br/judge/pt/problems/view/2807

# Resolução:

O objetivo deste problema é exibir a sequência de Fibonacci ao contrário (Iccanobif), a partir de um número que será recebido.

Para iniciar, declaramos as seguintes variáveis:
 * `N`, que será o tamanho da sequência de Fibonacci desejada;
 * `i`, que servirá para iterar sobre o laço de repetição;
 * `fibonacci`, que será um vetor de inteiros, utilizado para armazenar a sequência e depois exibi-la ao contrário.
```c
int N, i; 
int fibonacci[40];
```

Realizamos a leitura de `N` (tamanho da sequência desejada) com o comando `scanf` e inicializamos as duas primeiras posições de `fibonacci` com 1;
```c
scanf("%d", &N);
    
fibonacci[0]=1;
fibonacci[1]=1;
```

Em seguida, criamos um loop `for` para preencher o valor das proximas posições da sequência de Fibonnaci, até alcançar o valor de `N`.
```c
for(i=2; i<N; i++)
```
Note que o `for` começa em `2`, pois já inicializamos as duas primeiras posições do vetor (`fibonacci[0]` e `fibonacci[1]`).

Para preenchermos as próximas posições da sequência somamos os valores de 2 posições anteriores do vetor `fibonnaci`. Por isso, inicializamos suas duas primeiras posições com 1.
```c
fibonacci[i] = fibonacci[i-1] + fibonacci[i-2];
```

Após o preenchimento do vetor de Fibonacci, podemos imprimi-lo ao contrário. Isto é feito com um loop `for`, que será iniciado no tamanho do vetor `fibonacci` (`N-1`) e irá até a posição `0`.
```c
for(i = N-1; i>=0; i--){
``` 

Por fim, dentro do `for`, exibimos cada posição da sequência de Iccanobif com o comando `printf`.
```c
if(i>0)
	printf("%d ", fibonacci[i]);
            
else 
	printf("%d\n", fibonacci[i]);
```
Utilizamos uma estrutura `if` para que a saída seja no formato desejado pelo URI (último valor da sequência sem espaço).

##### Para aprender um pouco mais sobre o laço de repetição `for` : [for](http://linguagemc.com.br/a-estrutura-de-repeticao-for-em-c/)

Caso tenha alguma dúvida sobre este problema ou sobre a resolução, entre em contato com o PET-BCC pelo nosso
 * [Facebook](https://www.facebook.com/petbcc/),
 * [Instagram](https://www.instagram.com/petbcc.ufscar/)
 * ou nos mande um e-mail com o assunto "URI" para  petbcc.ufscar@gmail.com