# Problema:
Vinicius leva muito a sério seu condicionamento físico e, diariamente às 6h da manhã, chova ou faça sol, no verão e no inverno, ele corre no entorno de uma lagoa. Ao longo da pista de corrida existem N placas igualmente espaçadas. Para não desanimar do exercício, Vinicius conta o número de placas pelas quais ele já passou e verifica se ele já correu pelo menos 10%, pelo menos 20%, : : : , pelo menos 90% do percurso.

Vamos ajudar o Vinicius, calculando para ele o número de placas que ele precisa contar para ter completado pelo menos 10%, 20%, : : : , 90% da corrida, dados o número de voltas que ele pretende correr e o número total de placas ao longo da pista.

Por exemplo, suponhamos que Vinicius queira dar 3 voltas e o número de placas seja 17. Então, para garantir ter corrido pelo menos 30% do percurso, ele precisa contar 16 placas. Para garantir pelo menos 60%, ele precisa contar 31 placas.

**Problema Completo**: https://www.urionlinejudge.com.br/judge/pt/problems/view/2968

# Resolução:

Começamos com a declaração das variáveis, nesta resolução iremos utilizar 3 variáveis do tipo `int`, a variável `v` para armazenar o número de voltas, `p` para a quantidade de placas e `i` para usarmos como contador em nosso laço `for`. Após a declaração das variáveis realizamos a leitura do número de voltas e da quantidade de placas
```c
int v, p, i;
scanf("%d %d", &v, &p);
```

Para o laço de repetição usaremos a estrutura `for` iterando o valor presente em `i` de "1" até "9"
```c
for (i = 1; i < 10; ++i){
  ...
}
```

Para determinar qual placa representa 10% ... 90% da corrida iremos utilizar 2 operadores ternários que serão responsáveis por imprimir os valores em `"%d%c"`

No primeiro operador ternário iremos calcular quais serão as placas que indicarão o progresso da corrida, para isso, dentro de nosso `for` que irá iterar do valor "1" até "9", iremos realizar a seguinte operação:
 - `(i*v*p)%10 ? ((i*v*p)/10)+1 : (i*v*p)/10`
  - `(i*v*p)%10` irá realizar a divisão do valor resultante de `i*v*p`  por 10 e pegar o resto, caso esse seja maior do que "0" o operador ternário tratará isto como `TRUE` e irá incrementar "1" no resultado, caso contrário, ou seja, possui resto igual a "0", usaremos o resultado da operação `(i*v*p)/10`. Com isso iremos imprimir as 9 placas que indicam o progresso.

Juntamente com a determinação de qual placa será impressa, iremos definir se daremos um espaço entre as placas que serão impressas ou se não há mais placas a serem impressas.

- `i<9 ? ' ' : '\n'`
 - Caso não tenhamos mostrado todas as placas (i<9) iremos apenas dar um espaço para imprimir a próxima. Caso contrário, tendo todas as placas impressas, iremos inserir um `\n` ao final.

Valido lembrar que iremos trabalhar com apenas a parte inteira do resultado que iremos encontrar através das divisões, com isso nosso `printf` ficará:
```c
printf("%d%c", (i*v*p)%10 ? ((i*v*p)/10)+1 : (i*v*p)/10, i<9 ? ' ' : '\n');
```



##### Para revisar sobre: [Operador Ternário](http://excript.com/linguagem-c/operador-ternario-c.html)
    
Caso tenha alguma dúvida sobre este problema ou sobre a resolução, entre em contato com o PET-BCC pelo nosso
[Facebook](https://www.facebook.com/petbcc/),
[Instagram](https://www.instagram.com/petbcc.ufscar/)
ou nos mande um e-mail com o assunto "URI" para  petbcc.ufscar@gmail.com
