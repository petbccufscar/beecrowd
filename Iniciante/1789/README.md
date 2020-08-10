# Problema:
A corrida de lesmas é um esporte que cresceu muito nos últimos anos, fazendo com que várias pessoas dediquem suas vidas tentando capturar lesmas velozes, e treina-las para faturar milhões em corridas pelo mundo. Porém a tarefa de capturar lesmas velozes não é uma tarefa muito fácil, pois praticamente todas as lesmas são muito lentas. Cada lesma é classificada em um nível dependendo de sua velocidade:


Nível 1: Se a velocidade é menor que 10 cm/h .
Nível 2: Se a velocidade é maior ou igual a 10 cm/h e menor que 20 cm/h .
Nível 3: Se a velocidade é maior ou igual a 20 cm/h .


Sua tarefa é identificar qual nível de velocidade da lesma mais veloz de um grupo de lesmas.

**Problema Completo**: https://www.urionlinejudge.com.br/judge/pt/problems/view/1789


# Resolução:
É importante armazenarmos a primeira entrada para que então declaremos um vetor com tamanho equivalente a quantia de velocidades fornecida. Posteriormente, analisaremos seus valores com o objetivo de encontrar o maior e, assim, indicar o nível da lesma mais veloz.

Em um primeiro momento, declaramos apenas a variável inteira `L` para receber o número de lesmas fornecido.

```c
int L;
```

Conforme exemplificado no exercício, as entradas serão inseridas até que seja atingido o fim do arquivo, o qual é representado por `EOF`. Portanto, utilizamos a estrutura de repetição `while` para garantir que a leitura do primeiro valor de cada caso de teste será feita enquanto o arquivo não chegar ao fim.

```c
while(scanf("%d",&L) != EOF){
	...
}
```  

No interior desta estrutura, devemos realizar a leitura das demais entradas, encontrar aquela de maior valor e, por fim, verificar a qual nível pertence. Para isto, é necessário, primeiramente, declararmos o vetor `V` de tamanho `L` para armazenar os dados que serão fornecidos em sequência. A variável `i` servirá de auxílio logo em seguida.

```c
	int V[L];
	int i;
```

Usufruímos do comando `for` para efetuar a leitura da segunda linha do caso teste e guardar a velocidade de cada uma das `L` lesmas em uma posição diferente do vetor.

```c
for(i=0; i<L; i++){
	scanf("%d",&V[i]);
}
```

O método utilizado para encontrar o maior valor dentre os recém armazenados pode ser modularizado em uma função específica nomeada `buscaMaiorValor`. Para isto, declaramos o inteiro `maiorValor` e fazemos com que armazene o retorno desta função. Ao invocá-la, precisamos fornecer os dados necessários para seu funcionamento (neste caso, o vetor `V` e a variável `L`).

```c
int maiorValor = buscaMaiorValor(V, L);
```

A função é desenvolvida externamente à `main()` e, para elaborá-la, deve-se determinar qual o tipo de retorno que será fornecido, seguido de seu nome e, entre parênteses, os parâmetros a serem recebidos (lembrando de especificar seus tipos). Como citado anteriormente, seu tipo será `int` para que possa retornar o maior valor encontrado.
O vetor enviado deve conter um **asterisco** logo a sua esquerda, para que a função trabalhe com o **conteúdo** presente no local em que o ponteiro aponta. A variável `L` pode ser passada via cópia, pois será utilizada apenas de modo auxiliar.
Em seu interior, declaramos as variáveis inteiras: `posicao` (para guardar o índice do maior valor encontrado até então); `maiorValor` (para conter a velocidade mais alta); e `i`.  

```c
int buscaMaiorValor(int *V, int L){
	int posicao = 0;
	int maiorValor, i;
	...
}
```

Como próximo passo, percorremos cada uma das posições do vetor utilizando o comando `for`. Neste conterá a aplicação da estrutura `if` para verificar qual valor é maior: o que está guardado na posição corrente do vetor ou aquele cujo índice encontra-se em `posicao`. Caso seja o primeiro, as variáveis são atualizadas para que contenham os novos dados correspondentes ao maior valor. Em cenário contrário, `else` garante que o valor continue o mesmo e a posição deste não seja alterada.
Ao realizar todas as comparações necessárias, temos em `maiorValor` qual a máxima velocidade encontrada e, então, esta pode ser fornecida no retorno da função.

```c
for(i=0; i<L; i++){
	if(V[i] > V[posicao]){
		maiorValor = V[i];
		posicao = i;
	}

	else{
		maiorValor = V[posicao];
	}
}
return maiorValor;
```

Agora que possuímos a informação desejada, utilizamos, na função principal, três estruturas condicionais `if` para verificar em qual das exigências o resultado se adequa e, em seguida, exibir na tela o nível correspondente. Dessa forma, caso o valor contido em `maiorValor` seja inferior a 10, optamos pelo comando `printf()` exibindo o número '1'. No cenário em que a velocidade é maior ou igual a 10 e, simultaneamente, inferior a 20; mostramos o nível '2'. Por fim, caso seja maior ou igual a 20, exibimos '3'.  

```c
if(maiorValor < 10)
	printf("1\n");

if(maiorValor >= 10 && maiorValor < 20)
	printf("2\n");

if(maiorValor >= 20)
	printf("3\n");
```

##### Para aprender um pouco mais sobre fim de arquivos: [EOF](https://pt.wikipedia.org/wiki/EOF)

##### Para aprender um pouco mais sobre declaração de funções: [Funções em C](http://linguagemc.com.br/funcoes-em-c/)  

##### Para aprender um pouco mais sobre ponteiros: [Programar em C/Ponteiros](https://pt.wikibooks.org/wiki/Programar_em_C/Ponteiros)

Caso tenha alguma dúvida sobre este problema ou sobre a resolução, entre em contato com o PET-BCC pelo nosso [Facebook](https://www.facebook.com/petbcc/), [Instagram](https://www.instagram.com/petbcc.ufscar/) ou nos mande um e-mail com o assunto "URI" para  petbcc.ufscar@gmail.com
