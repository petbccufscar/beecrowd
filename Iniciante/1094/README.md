# Problema:    
Maria acabou de iniciar seu curso de graduação na faculdade de medicina e precisa de sua ajuda para organizar os experimentos de um laboratório o qual ela é responsável. Ela quer saber no final do ano, quantas cobaias foram utilizadas no laboratório e o percentual de cada tipo de cobaia utilizada.

Este laboratório em especial utiliza três tipos de cobaias: sapos, ratos e coelhos. Para obter estas informações, ela sabe exatamente o número de experimentos que foram realizados, o tipo de cobaia utilizada e a quantidade de cobaias utilizadas em cada experimento.  

Conforme a entrada exemplificada no exercício, "a primeira linha contém um valor inteiro **N** que indica os vários casos de teste que vem a seguir. Cada caso de teste contém um inteiro **Quantia** (1 ≤ Quantia ≤ 15) que representa a quantidade de cobaias utilizadas e um caractere **Tipo** ('C', 'R' ou 'S'), indicando o tipo de cobaia (*R*:Rato *S*:Sapo *C*:Coelho).

**Problema Completo**: https://www.urionlinejudge.com.br/judge/pt/problems/view/1094


# Resolução:
Para solucionar este exercício, podemos utilizar a primeira entrada fornecida (quantidade de casos de teste) para limitar um loop, no qual cada caso é lido e seus dados são armazenados separadamente. Ao final, realizamos as contas necessárias para obter o resultado.

Como já sugerido pelo enunciado, criamos as variáveis inteiras `N` e `Quantia` para conter, respectivamente, o número de casos de teste e a quantidade de cobaias a serem fornecidos na entrada. Além disso, é necessário uma variável do tipo `char` para armazenar a sigla fornecida no caso de teste e, como exemplificado, será nomeada `Tipo`.   
Visto que o resultado exigirá a soma da quantia de cada cobaia, bem como o total, declaramos 4 variáveis `int` para guardar cada um destes valores. Vale destacar que devem ser inicializados com 0 para não prejudicar o incremento que será realizado posteriormente.
Também é necessário uma do tipo `float` (pois exigiu-se a representação com casas decimais), em que será armazenado o percentual obtido.

```c
int N=0, Quantia;
int coelhos=0, ratos=0, sapos=0, total=0;
int i;
float percentual;
char Tipo;
```

Para receber a primeira entrada, utilizamos a função `scanf()` para armazená-la em `N`. Após já termos esse valor em mãos, é possível realizar o loop `for` que itere de acordo com a quantia de casos de teste. Assim, a estrutura de repetição conterá, primeiramente, a leitura dos 2 valores informados em cada caso. Como trata-se de um inteiro e uma cadeia de caractere (nesta ordem), a função `scanf()` possui como argumentos `%d` e `%c`.

```c
for(i=0; i<N; i++){
  scanf("%d %c",&Quantia,&Tipo);
  ...
}//chave referente ao laço for
```

**Ainda dentro do loop**, utilizamos 3 funções `if` para conferir qual caractere foi digitado na entrada em questão. Caso tenha sido *C* (ou seja, a variável `Tipo` contém este caractere), iremos incrementar o valor de `Quantia` ao que já está armazenado na variável `coelhos`. Desse modo, quando o `for` encerrar-se, teremos nela a quantidade total de coelhos utilizados.
O mesmo cenário ocorre para as demais cobaias no caso em que o caractere seja *R* ou *S*, como representado nas demais estruturas de decisão.

```c
if(Tipo == 'C'){
  coelhos = coelhos + Quantia;
}

if(Tipo == 'R'){
  ratos = ratos + Quantia;
}

if(Tipo == 'S'){
  sapos = sapos + Quantia;
}
}//chave referente ao término do laço for
```

Neste momento, fazemos com que a variável `total` contenha a quantidade de coelhos, ratos e sapos; através da soma destes. Ademais, exibimos tais resultados na tela com a função `printf()`.

```c
total = coelhos+ratos+sapos;

printf("Total: %d cobaias\n",total);
printf("Total de coelhos: %d\n",coelhos);
printf("Total de ratos: %d\n",ratos);
printf("Total de sapos: %d\n",sapos);
```

Usufruímos da variável `percentual` para guardar, periodicamente, a porcentagem de cada cobaia diante do total obtido. Para isto, realizamos o [cálculo da porcentagem](https://www.todamateria.com.br/calcular-porcentagem/) através da multiplicação da cobaia em questão por 100.00 e, em seguida, a divisão pelo `total`. É importante que o número seja representado de forma decimal para que o resultado obtido também seja um número decimal, uma vez que isto foi exigido pelo exercício.
Logo depois, o resultado percentual obtido pode ser mostrado na tela através do `printf()`, o qual deverá conter como argumento `%.2f`, pois isto garante que o valor `float` será exibido com 2 casas após o ponto. Vale destacar, também, a utilização de `%%` propositalmente duplicada para que a função saiba que não se trata de um argumento e, assim, exibirá o caractere % na tela.
Este mesmo procedimento é feito para cada uma das cobaias existentes, sendo importante projetar a saída antes que `percentual` seja sobrescrito para a próxima cobaia.

```c
percentual = (coelhos*100.00)/total;
printf("Percentual de coelhos: %.2f %%\n",percentual);

percentual = (ratos*100.00)/total;
printf("Percentual de ratos: %.2f %%\n",percentual);

percentual = (sapos*100.00)/total;
printf("Percentual de sapos: %.2f %%\n",percentual);
```

##### Para aprender um pouco mais sobre cadeia de caracteres: [STRINGS](https://www.ic.unicamp.br/~norton/disciplinas/mc1022s2005/06_10.html)

##### Para aprender um pouco mais sobre a estrutura for: [O laço FOR](https://www.cprogressivo.net/2013/02/O-que-e-para-que-serve-e-como-usar-o-laco-FOR-em-C.html)  

Caso tenha alguma dúvida sobre este problema ou sobre a resolução, entre em contato com o PET-BCC pelo nosso [Facebook](https://www.facebook.com/petbcc/), [Instagram](https://www.instagram.com/petbcc.ufscar/) ou nos mande um e-mail com o assunto "URI" para  petbcc.ufscar@gmail.com
