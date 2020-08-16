# Problema:
Após comprar vários sítios adjacentes na região do oeste catarinense, a família Estrela construiu uma única estrada que passa por todos os sítios em sequência. O primeiro sítio da sequência foi batizado de Estrela 1, o segundo de Estrela 2, e assim por diante. Porém, o irmão que vive em Estrela 1 acabou enlouquecendo e resolveu fazer uma Jornada nas Estrelas para roubar carneiros das propriedades de seus irmãos. Mas ele está definitivamente pirado. Quando passa pelo sítio Estrela i, ele rouba apenas um carneiro daquele sítio (se o sítio tem algum) e segue ou para Estrela i + 1 ou para Estrela i - 1, dependendo se o número de carneiros em Estrela i era, respectivamente, ímpar ou par. Se não existe a Estrela para a qual ele deseja seguir, ele interrompe sua jornada. O irmão louco começa sua Jornada em Estrela 1, roubando um carneiro do seu próprio sítio.
 
 
##### Link do problema: https://www.urionlinejudge.com.br/judge/pt/problems/view/1973
 
 
# Resolução:
 
Iremos pontuar certas informações importantes do enunciado:
- O sítio inicial será a Estrela 1;
- O número de carneiros da estrela que está sendo roubada define qual será a próxima estrela a roubar:
    - se for par, a próxima estrela é a da esquerda (`i - 1`)
    - se for ímpar, a próxima estrela é a da direita (`i + 1`)
- A jornada de roubo termina quando a próxima estrela que ele deseja ir não existe. Isto é, quando ele for roubar a estrela 1 e houver um número par de carneiros, o próximo destino seria a estrela 0. Ou quando ele for roubar a última estrela e houver um número ímpar de carneiros, o próximo destino seria a estrela N + 1.

Além disso, o programa pede o número de estrelas atacadas e o número de carneiros não roubados. Com isso,iremos declarar as seguintes variáveis do tipo `long long int`:  `N`, `total = 0`, `ataques = 0`, `i`, `j` e `impar`. A variável `total` será utilizada para contabilizarmos o total de carneiros não roubados e `impar` para sabermos se o número de carneiros da estrela é impar ou par, para sabermos a próxima estrela destino. 
 
```c
long long int N, total = 0, ataques = 0, i, j;
long long int impar;
```

Depois, lemos o valor de `N`, por meio da função `scanf()`.

```c
scanf("%lld", &N);
```

Agora, iremos declarar dois vetores com tamanho igual a quantidade de estrelas, `N`. O primeiro, para armazenarmos a quantidade de carneiros que cada estrela tem. O segundo, para nos auxiliar a saber se tal estrela já foi atacada e para isso, inicializamos-o com 0 em todas as posições e caso uma estrela seja atacada, mudamos para 1. Porém, como não sabemos o tamanho de `N` na hora de compilar o programa, é incorreto declarar um vetor de tamanho `N` de forma estática. Por isso, iremos utilizar alocação dinâmica, que no nosso caso consiste em reservar na memória um espaço equivalente ao tamanho de uma variável do tipo `long long int` multiplicada por N e esses serão nossos vetores .

```c
long long int* estrelas = (long long int*)malloc(N * sizeof(long long int));
long long int* atacada = (long long int*)malloc(N * sizeof(long long int));
```

Em seguida, utilizaremos uma estrutura de repetição `for` que irá iterar `N` vezes, uma para cada estrela. 

A cada iteração do laço de repetição:
- lê a quantidade de carneiros da estrela;
- adiciona esse número de carneiros lido ao total de carneiros, `total`;
- atribui zero na posição da estrela no vetor alocado dinâmicamente.

```c
for (i = 0; i < N; i++){
		scanf("%lld", &estrelas[i]);
		total += estrelas[i];
		atacada[i] = 0;

	}
```

Em seguida, iremos iniciar o roubo dos carneiros. A variável `j` indica em qual estrela o irmão está atualmente. O ponto inicial será sempre a primeira estrela, por isso incializamos `j` com 0 `j = 0`.

Caso o fazendeiro tente ir para uma estrela antes da primeira, ou depois da última estrela, o programa encerra. Por conta disso, a condição da estrutura de repetição `while` que usaremos será `while(j >= 0 && j < N )`.

A cada iteração do laço de repetição:
- atribuímos o resto da divisão do número de carneiros por 2 (`estrelas[j]%2`) a variável `impar` para obtermos a paridade do número de carneiros da estrela atual, pois como se trata de uma divisão por 2, o resto poderá ser apenas 0 ou 1.
- se a quantidade de carneiros da estrela vigente for maior que zero, o irmão rouba um carneiro:
    - diminuímos em 1 a quantidade de carneiros da estrela e também do total
    - verificamos se tal estrela já não foi atacada. Caso ainda não tenha sido, aumentamos em 1 o número de estrelas atacadas e mudamos o valor desta estrela no vetor de atacadas de 0 para 1
- por fim, o irmão passa para a próxima estrela:
    - se `impar` for 1, ou seja, a quantidade de carneiros antes do roubo era ímpar, adicionamos 1 a `j`;
    - se `impar` for 0, ou seja, a quantidade de carneiros antes do roubo era par, subtraímos 1 a `j`;

```c
j = 0;
while(j >= 0 && j < N ){

    impar = estrelas[j] % 2 ;
		
    if( estrelas[j] > 0){

		estrelas[j]--;
		total--;

		if(atacada[j] == 0){

			ataques++;
			atacada[j] = 1;
		}

	}

   	if(impar)
    	    j++;
        else
	    j--;
		
	
}

Quando a jornada de roubos acaba, ou seja, quando `j` for -1 ou `N`, exibimos a quantidade de estrelas atacadas e a quantidade de carneiros não roubados, `ataques` e `total` respectivamente.

```c
printf("%lld %lld\n", ataques, total);
```
 
Caso tenha alguma dúvida sobre este problema ou sobre a resolução, entre em contato com o PET-BCC pelo nosso
[Facebook](https://www.facebook.com/petbcc/),
[Instagram](https://www.instagram.com/petbcc.ufscar/)
ou nos mande um e-mail com o assunto "URI" para  petbcc.ufscar@gmail.com
