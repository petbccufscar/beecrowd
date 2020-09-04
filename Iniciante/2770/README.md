# Problema

Acontece que para ser fabricado, o circuito do pedal é impresso em uma PCI(placa de circuito impresso), que tem um certo tamanho. Porém com a criatividade dos clientes, as placas estão tomando dimensões inimagináveis, tal fato faz com que a placa disponível na empresa não sirva. Como você é um excelente programador e um amante da música, cabe a você criar um programa em que dada as dimensões do circuito do cliente e a dimensão da placa disponível, diga se é possível utilizar ou não aquela placa.

##### Problema completo: https://www.urionlinejudge.com.br/judge/pt/problems/view/2770

# Resolução

Para resolver o problema, iremos verificar se o tamanho de placa provido pela fábrica é compatível com o pedido pelo cliente, retornando "Sim" ou "Não" para cada caso.

Começamos declarando nossas variáveis que serão utilizadas no problema, todas do tipo inteiro. Serão elas: 
- `alturaPlaca`, para a altura da placa da fábrica, denominada X no enunciado;
- `larguraPlaca`, para a largura da placa da fábrica, denominada Y no enunciado;
- `qtsPedidos`, para a quantidade de pedidos, denominada M no enunciado;
- `alturaPci`, para a altura da placa do cliente, denominada Xi no enunciado; 
- `larguraPci`, para a largura da placa do cliente, denominada Yi no enunciado;
- `i`, para iterar nas estruturas de repetição.

```c
	int alturaPlaca, larguraPlaca, qtsPedidos;
	int alturaPci, larguraPci, i;
```

Inicializamos a estrutura de repetição `while`, com a leitura de EOF da estrutura `scanf` como critério de parada. 
```c
	while (scanf("%d %d %d", &alturaPlaca, &larguraPlaca, &qtsPedidos) != EOF)
```

Agora, inicializamos a estrutura de repetição `for`, utilizando a variável `i` para realizar as iterações, até atingit a quantidade de pedidos em `qtdPedidos`.
```c
	for (i = 0; i < qtsPedidos; i++)
```

Faremos a leitura das dimensões da placa do cliente com `scanf`.
```c
        scanf("%d %d", &alturaPci, &larguraPci);
```

Em seguida, faremos as comparações para verificar se a placa da fábrica é compatível com os pedidos dos clientes. Em ambos casos, verificamos se as áreas são acordantes.
Caso as dimensões da placa da fábrica (representadas pos `alturaPlaca` e `larguraPlaca`) sejam maiores ou iguais às pedidas pelo cliente (em `alturaPci` e `larguraPci`), a placa pode ser utilizada.
Em outro caso, temos que as alturas e larguras não são compatíveis entre si, mas formam uma área compatível. Portanto, caso a largura em `larguraPlaca` seja maior ou igual que a `alturaPci` e a altura em `alturaPlaca` seja maior ou igual a `larguraPci`, continuamos tendo uma área aceitável. 

Faremos a representação destes casos com a estrutura condicional `if`. Caso esteja nessas condições, exibimos `sim` com a estrutura `printf`. Caso contrário, exibimos `não`.
```c
		if ((alturaPci <= alturaPlaca && larguraPci <= larguraPlaca) || (alturaPci <= larguraPlaca && larguraPci <= alturaPlaca))
			printf("Sim\n");
		else
			printf("Nao\n");
```

Caso tenha alguma dúvida sobre este problema ou sobre a resolução, entre em contato com o PET-BCC pelo nosso
[Facebook](https://www.facebook.com/petbcc/),
[Instagram](https://www.instagram.com/petbcc.ufscar/)
ou nos mande um e-mail com o assunto "URI" para  petbcc.ufscar@gmail.com