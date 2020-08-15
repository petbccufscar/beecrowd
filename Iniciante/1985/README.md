# Problema:    
O MacPRONALTS está com uma super promoção, exclusivo para os competidores da primeira Seletiva do MaratonaTEC. Só que teve um problema, todos os maratonistas foram tentar comprar ao mesmo tempo, com isso gerou uma fila muito grande. O pior é que a moça do caixa estava sem calculadora ou um programa para ajudá-la a calcular com maior agilidade, eis que surge você para fazer um programa para ajudar a coitada e aumentar a renda do MacPRONALTS. Segue o cardápio do dia contendo o número do produto e seu respectivo valor.  
1001 | R$ 1.50  
1002 | R$ 2.50  
1003 | R$ 3.50  
1004 | R$ 4.50  
1005 | R$ 5.50

**Problema completo**: https://www.urionlinejudge.com.br/judge/pt/problems/view/1985


# Resolução:
Para resolver este exercício, vamos receber a quantidade de códigos de produto e, por sua vez, a quantidade de cada produto. Devemos multiplicar a quantidade de cada por seu respectivo valor e exibir o valor total de produtos.

Inicialmente, declaramos as variáveis necessárias para o problema. A variável `produtos` irá armazenar quantos produtos diferentes vamos ler, enquanto `codigo` e `quantidade` serão usadas para calcular o `total` - uma variável do tipo `float` já que os preços possuem casas decimais. Há também uma variável `i` para percorrer um loop.  
Obs: como o `total` será incrementado, é importante inicializar a variável com 0;

```c
int produtos, codigo, quantidade, i;
float total = 0;
```

Para receber os produtos, vamos utilizar um loop `for` e, para cada produto, armazenar seu código e sua quantidade. Não precisamos nos preocupar com os caracteres que são inseridos no meio, como | e o R$, já que a função `scanf` com `%d` procura apenas por números inteiros.

```c
for (i = 0; i < produtos; i++) {
    scanf("%d %d", &codigo, &quantidade);

    /*
        calculo do total
    */
}
```

O total será calculado a partir de `if`'s. Verificando o código correspondente do produto, multiplicamos a quantidade por seu valor e somamos na variável `total`.

```c
if (codigo == 1001)
    total += quantidade * 1.5;

else if (codigo == 1002)
    total += quantidade * 2.5;

else if (codigo == 1003)
    total += quantidade * 3.5;

else if (codigo == 1004)
    total += quantidade * 4.5;

else if (codigo == 1005)
    total += quantidade * 5.5;
```
###### Note que, como as condicionais possuem apenas uma linha dentro de cada, podemos omitir as chaves `{}`. Em códigos maiores, esta sintaxe não é recomendada.

Por fim, exibimos o `total` formatado com duas casas decimais, a partir do argumento `%.2f`.

```c
printf("%.2f\n", total);
```

##### Para relembrar sobre o laço for: [O comando for](http://linguagemc.com.br/a-estrutura-de-repeticao-for-em-c/)
##### Para aprender mais sobre variáveis de ponto flutuante: [Os tipos float e double](https://www.cprogressivo.net/2012/12/Os-tipos-float-e-double-numeros-decimais-reais-em-C.html)

Caso tenha alguma dúvida sobre este problema ou sobre a resolução, entre em contato com o PET-BCC pelo nosso
[Facebook](https://www.facebook.com/petbcc/),
[Instagram](https://www.instagram.com/petbcc.ufscar/)
ou nos mande um e-mail com o assunto "URI" para  petbcc.ufscar@gmail.com
