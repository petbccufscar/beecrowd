# Problema:

Em 2013 a Feira FACE compactou os dados de seus visitantes com um compactador livre, infelizmente esta ferramenta se tornou paga e você foi convidado a criar um algoritmo para descompactar os dados. Os dados estão compactados em formato decimal, e para funcionar o descompactador você terá que encontrar o dígito verificador de cada linha compactada. A organização da FACE conseguiu uma documentação de como funcionava o processo, mas algumas informações de como chegar ao dígito não estão muito claras, o documento apenas disponibiliza alguns exemplos, conforme segue:

- Linha compactada composta por 54782 ao descompactar iria resultar na cadeia binária 00000111100000001111111100, com isso o valor do dígito ficaria 8.
- Linha compactada composta por 045 ao descompactar iria resultar na cadeia binária 111100000, com isso o valor do dígito ficaria 9.

**Problema completo:** https://www.urionlinejudge.com.br/judge/pt/problems/view/1629


# Resolução: 
Inicialmente, na função `main` declaramos uma varíavel `s` do tipo string, de tamanho máximo *1000*, e dois inteiros, `tamanho` e `casos`.
``` c
    char s[1000];
    int tamanho, casos;
```

Logo após as declarações, temos um loop que será executado e irá realizar a leitura enquanto o valor lido for diferente de zero.
``` c
    while (1)
	{
		scanf("%d", &casos);
		if (casos == 0) return 0; 
		...
	}
```
Em seguida há um outro `while` que realizará as operações principais do código, que funcionam da seguinte maneira:
- Primeiro será realizada a leitura do conjunto de valores, armazenando-os numa string e logo após serão contados quantos valores existem no conjunto com a função `strlen()`;
- A seguir será contada a quantidade de *uns* e *zeros* utilizando dois `for` seguidos. Por exemplo: no número *45*, como o número *4* está na primeira posição, descompactamos transformando em *0000*, para o *5* transformamos em *11111* e seguimos alternando entre os *zeros* e *uns*;
- Após a contagem, será chamada a função `somaDigitos` duas vezes, para somar os dígitos *uns* e os *zeros*. Por exemplo: se tivessemos *14 zeros* e *12 uns*, essa função retornaria respectivamente *5* e *3*. Por fim, imprime-se a soma total, que no caso do exemplo citado, seria *8*.
``` c
    while (casos--)
	{
		scanf("%s", s);
        tamanho = strlen(s);
		
		int uns = 0;
		int zeros = 0;
		for (int i = 0 ; i < tamanho; i += 2)
			zeros += (s[i] - '0');
		for (int i = 1 ; i < tamanho; i += 2)
			uns += (s[i] - '0');
		
		zeros = somaDigitos(zeros);
		uns = somaDigitos(uns);
		
		printf("%d\n", zeros + uns);
	}
```
A função `somaDigitos` recebe um parâmetro `n` que é um número inteiro, e soma cada dígito fazendo a operação de módulo/resto da divisão por *10* para isolar o menos significativo. Em seguida, ele faz a divisão inteira por *10* para ficar apenas com os dígitos seguintes. Por exemplo, utilizando o número *123*, fazemos *123 % 10 = 3*, isolando o menos significativo, depois atualizamos `n` para *123/10 = 12*, ficando com os demais.

``` c
  int somaDigitos(int n)
  {
	 int soma = 0;
	
	 while (n > 0)
	 {
		soma += (n % 10);
		n /= 10;
	 }
	 return soma;
  }
```


Caso tenha alguma dúvida sobre este problema ou sobre a resolução, entre em contato com o PET-BCC pelo nosso
[Facebook](https://www.facebook.com/petbcc/),
[Instagram](https://www.instagram.com/petbcc.ufscar/)
ou nos mande um e-mail com o assunto "URI" para  petbcc.ufscar@gmail.com