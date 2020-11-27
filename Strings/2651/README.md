# Problema:

Link é um herói famoso e por isso recebe diversas cartas de seus fãs. Porém mesmo sendo famoso, todos continuam o chamando de Zelda.

Por causa disso Link está muito bolado, tão bolado que sempre que recebe uma carta ele confere como o seu fã se referiu a ele na carta, e caso ele perceba o trecho "zelda" no nome ele fica bolado e joga a carta fora.

Sua tarefa é determinar se Link ficará bolado com a forma que seu fã o chamou na carta ou não.

**Problema completo:** https://www.urionlinejudge.com.br/judge/pt/problems/view/2651


# Resolução: 
Inicialmente, na função `main`, declaramos uma variável `nome` do tipo string, de tamanho máximo *100001*, como requerido no enunciado, que representa como o fã do Link se referiu a ele na carta.
``` c
    char nome[100001];
```

Logo após a declaração, será realizada a leitura desse nome.
``` c
    scanf("%s", nome);
```
Após a leitura, iremos checar se seu nome foi lido como *'zelda'* por meio da função `temZelda`, caso não tenha sido, será exibido na tela a frase "Link Tranquilo", caso contrário a frase exibida será "Link Bolado".
``` c
  	if (!temZelda(nome))
		printf("Link Tranquilo\n");
	else
		printf("Link Bolado\n");
```

A função `temZelda` chamada na `main` recebe como parâmetro um ponteiro para `nome`.
```c
	int temZelda(char *nome)
```

E dentro dela são declarados três contadores `i`, `j` e `contador` utilizados no `for` e uma string `comparacao` que recebe o nome "zelda".
```c
	int i, j, contador = 0;
	char comparacao[6] = "zelda";
```

Por meio do loop `for` temos a parte principal do programa, que compara o nome lido com o vetor `comparacao` que contém a palavra "zelda". A cada iteração verificamos se a i-ésima letra do `nome` é igual a j-ésima letra em `comparacao`, caso seja, avançamos o j e incrementamos o contador, indicando que já temos uma letra igual. Caso seja diferente, tanto o `contador` quanto o `j` retornam a *0* (indicando que voltamos a procurar a letra 'z' no nome). 
No `if` que compara `nome[i]` e `comparacao[j]` também comparamos o valor com *+ 32* e *- 32*, já que `'A' = 65` e `'a' = 97` em ASCII. Portanto, somando e subtraindo 32 também consideramos casos em que alguma letra está maiúscula.
```c
	for (i = 0, j = 0; nome[i]; i++)
	{	
		if (nome[i] == comparacao[j] || 
		nome[i] == comparacao[j] + 32 || 
		nome[i] == comparacao[j] - 32)
		{
			j++;
			contador++;

			if (contador == 5)
				return 1;
		}
		else
		{
			contador = 0;
			j = 0;
		}
	}
```

**Saiba mais sobre ponteiros em: [Endereços e ponteiros](https://www.ime.usp.br/~pf/algoritmos/aulas/pont.html)**

**Saiba mais sobre tabela ASCII em: [Tabela ASCII](https://web.fe.up.pt/~ee96100/projecto/Tabela%20ascii.htm)**

Caso tenha alguma dúvida sobre este problema ou sobre a resolução, entre em contato com o PET-BCC pelo nosso
[Facebook](https://www.facebook.com/petbcc/),
[Instagram](https://www.instagram.com/petbcc.ufscar/)
ou nos mande um e-mail com o assunto "URI" para  petbcc.ufscar@gmail.com
