# Problema:

Em um país imaginário denominado Lisarb, todos os habitantes ficam felizes em pagar seus impostos, pois sabem que nele não existem políticos corruptos e os recursos arrecadados são utilizados em benefício da população, sem qualquer desvio. A moeda deste país é o Rombus, cujo símbolo é o R$.

Leia um valor com duas casas decimais, equivalente ao salário de uma pessoa de Lisarb. Em seguida, calcule e mostre o valor que esta pessoa deve pagar de Imposto de Renda, segundo a tabela abaixo.

	Renda							Imposto de Renda
	de 0.00 a R$ 2000.00					Isento
	de 2000.01 até R$ 3000.00				 8 %
	de 3000.01 até R$ 4500.00				 18 %
	acima de 4500.00					 28 %

Lembre que, se o salário for R$ 3002.00, a taxa que incide é de 8% apenas sobre R$ 1000.00, pois a faixa de salário que fica de R$ 0.00 até R$ 2000.00 é isenta de Imposto de Renda. No exemplo fornecido (abaixo), a taxa é de 8% sobre R$ 1000.00 + 18% sobre R$ 2.00, o que resulta em R$ 80.36 no total. O valor deve ser impresso com duas casas decimais.

###### Problema completo: https://www.urionlinejudge.com.br/judge/pt/problems/view/1051

# Resolução:

Iniciaremos declarando as variaveis que serão utilizadas, dessa vez usaremos a variavel "salario" para armazenar o valor que será inserido e a variavel "imposto" onde sera, após os calculos, armazenado o valor final que será exibido. Para isso faremos:
```c
        float salario, imposto;
```

Para leitura do salario, usamos a função scanf:
```c
        scanf("%f", &salario);
```

No primeiro caso iremos tratar dos salários que estão entre R$0.00 e R$2000.01
Nesse caso basta que, caso o salário esteja dentro dessa margem, apenas iremos dar um print com "Isento"
```c
    if (salario >= 0 && salario <= 2000.01)
		printf("Isento\n");
```

No segundo caso iremos tratar dos salários que estão entre R$2000.01 e R$3000.00
Nesse caso iremos desconsiderar os 2000 que são isentos e calcula 8% apenas sobre o valor que sobrou
```c
	if (salario > 2000 && salario <= 3000){
	    imposto = ((salario-2000) * 0.08);
	    printf("R$ %.2f\n", imposto); 
	}
```

No terceiro caso iremos tratar dos salários que estão entre R$3000.01 e R$4500.00
Alem dos 2000 que são isentos iremos calcular 8% sobre 1000.00 dentro da condição anterior (R$2000.01 ~~ R$3000.00)
E mais ainda calcularemos 18% do que sobrou, que está entre R$3000.01 e R$4500.00
```c
	if ( salario > 3000 && salario <= 4500){
	    imposto =( (1000*0.08) + ((salario-3000)*0.18) );
	    printf("R$ %.2f\n", imposto);
	}
```

No ultimo caso iremos tratar dos salários que são maiores que R$4500.00.
Nesse caso, assim como os anteriores, calcularemos 8% sobre R$1000.00. (R$2000.01 ~~ R$3000.00)
Calcularemos agora 18% sobre R$1500.00 (R$3000.01 ~~ R$4500.00)
E por final calcularemos 28% do que sobrou, sobre a parte que é maior que R$4500.00
```c
    if ( salario > 4500){
	    imposto = ( (1000*0.08) + (1500*0.18) + ((salario-4500)*0.28) );
	    printf("R$ %.2f\n", imposto);
	}
```

###### Todas as funções utlizadas estão contidas na biblioteca stdio.h, incluída na primeira linha do nosso programa.