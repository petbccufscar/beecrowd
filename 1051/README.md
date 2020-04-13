# Problema:

Em um país imaginário denominado Lisarb, todos os habitantes ficam felizes em pagar seus impostos, pois sabem que nele não existem políticos corruptos e os recursos arrecadados são utilizados em benefício da população, sem qualquer desvio. A moeda deste país é o Rombus, cujo símbolo é o R$.

Leia um valor com duas casas decimais, equivalente ao salário de uma pessoa de Lisarb. Em seguida, calcule e mostre o valor que esta pessoa deve pagar de Imposto de Renda, segundo a tabela abaixo.

	Renda							Imposto de Renda
	de 0.00 a R$ 2000.00				Isento
	de 2000.01 até R$ 3000.00			 8 %
	de 3000.01 até R$ 4500.00			 18 %
	acima de 4500.00					 28 %

Lembre que, se o salário for R$ 3002.00, a taxa que incide é de 8% apenas sobre R$ 1000.00, pois a faixa de salário que fica de R$ 0.00 até R$ 2000.00 é isenta de Imposto de Renda. No exemplo fornecido (abaixo), a taxa é de 8% sobre R$ 1000.00 + 18% sobre R$ 2.00, o que resulta em R$ 80.36 no total. O valor deve ser impresso com duas casas decimais.

###### Problema completo: https://www.urionlinejudge.com.br/judge/pt/problems/view/1051

# Resolução:

Para ler os 4 valores inteiros antes precisamos declará-los como variáveis, para isso fazemos:
```c
        int A, B, C, D, X;
```

No nosso caso, em "X" será armazenado o resultado que ao final será exibido na tela.

Para leitura, usamos a função scanf:
```c
        scanf("%d %d %d %d",&A, &B, &C, &D);
```
Dessa forma realizamos a leitura de todos os valores. 

Agora fazemos uma atribuição a variável "X" realizando a diferença entre os produtos de AB e CD.
```c
        X = (A * B - C * D);
```
E por fim, escrevemos o resultado na tela utilizando a função printf:
```c
        printf("DIFERENCA = %d\n",X);
```
%d será substituido pelo valor contido em X.

###### Todas as funções utlizadas estão contidas na biblioteca stdio.h, incluída na primeira linha do nosso programa.


