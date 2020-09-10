# Problema:
A fim de parar a greve geral dos estudantes, o governo realizou uma reunião com a UFSC. Durante a reunião a UFSC expôs todos os gastos necessários para manter o funcionamento até o final do ano e o Governo informou valores que poderia oferecer para cobrir esses gastos. A reunião não foi muito organizada, e vários valores individuais foram mencionados, de forma que ninguém sabe se os valores oferecidos são suficientes para cobrir todos os gastos da universidade.

Dada a lista de valores citados na reunião, sua tarefa será somas os gastos e as verbas oferecidas para informar os estudantes da UFSC se a greve deve parar ou não.

**Problema Completo**: https://www.urionlinejudge.com.br/judge/pt/problems/view/2982

# Resolução:


Iniciamos declarando as variáveis, `op` do tipo `char` para lermos qual foi a operação "G" ou "V", a variável `i` para usarmos como contador em nosso laço `for`, `n` que irá armazenar o numero de valores citados na reunião, `valor` para a cada iteração ler o valor que foi oferecido ou gasto e `total` para irmos contabilizando estas operações, inicializamos total com o valor "0" para garantir que não vai ficar nenhum lixo de memória armazenado.
Na função `scanf` realizamos a leitura do número de valores e iremos precisar utilizar o parâmetro `%*c`, o que ele faz é ler um caractere e descartá-lo, precisamos coloca-lo por conta do compilador "gcc".

```c
char op;
int i, n, valor, total = 0;
scanf("%d%*c", &n);
```

Em nosso laço principal realizamos a leitura da operação que for realizada, seja ela "G" ou "V", e em seguida o valor da mesma. Após isso caso a operação seja igual a "G" subtraímos o valor da quantia presente em `total`, caso contrario incrementamos este valor ao total.
```c
for (i = 0; i < n; ++i){
  scanf("%c %d%*c", &op, &valor);

  if (op == 'G')
  	total -= valor;
  else
  	total += valor;
}
```

Ao final verificamos se o valor contido em `total` possui valor positivo, ou seja o dinheiro recebido foi suficiente para cobrir os gastos, ou se possui um valor negativo, indicando dívida, e imprimimos de acordo com a formatação proposta pelo problema

```c
if (total >= 0)
	printf("A greve vai parar.\n");
else
	printf("NAO VAI TER CORTE, VAI TER LUTA!\n");
```

    
Caso tenha alguma dúvida sobre este problema ou sobre a resolução, entre em contato com o PET-BCC pelo nosso
[Facebook](https://www.facebook.com/petbcc/),
[Instagram](https://www.instagram.com/petbcc.ufscar/)
ou nos mande um e-mail com o assunto "URI" para  petbcc.ufscar@gmail.com