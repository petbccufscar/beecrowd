# Problema:    
Um Posto de combustíveis deseja determinar qual de seus produtos tem a preferência de seus clientes. Escreva um algoritmo para ler o tipo de combustível abastecido (codificado da seguinte forma: 1.Álcool 2.Gasolina 3.Diesel 4.Fim). Caso o usuário informe um código inválido (fora da faixa de 1 a 4) deve ser solicitado um novo código (até que seja válido). O programa será encerrado quando o código informado for o número 4.

**Problema completo**: https://www.urionlinejudge.com.br/judge/pt/problems/view/1134


# Resolução:
Para resolver o exercício, devemos ler os valores digitados até que seja lido o número `4`. Utilizaremos um laço `while` para isso, porém com uma pequena variação: `do{} while()`.  
Na primeira execução, precisamos ler o valor antes de poder verificá-lo. Logo, a primeira instrução deve ser um `scanf()`. Se isso fosse feito com um `while()` comum, precisaríamos ler o valor fora do laço, verificar, e ler de novo ao final do laço para a próxima iteração - o que funciona, mas gera repetição de código.  


Começamos declarando as variáveis que vamos precisar. Três para guardar os tipos de combustíveis do exercício e uma pra ler a `entrada` do programa.
```c
int alcool, gasolina, diesel, entrada;
```

Em seguida, precisamos inicializar os combustíveis como 0.
```c
alcool = 0;
gasolina = 0;
diesel = 0;
```

O código abaixo lê a `entrada` e verifica se ela corresponde a `1`, `2` ou `3`. Se sim, aumenta uma quantidade do combustível correspondente.  
Por último, verifica se o valor era um `4`:
- Se sim, termina o laço de repetição
- Se não, volta a ler a entrada
```c
do {
    scanf("%d", &entrada);

    if(entrada == 1)
        alcool++;
    else if(entrada == 2)
        gasolina++;
    else if(entrada == 3)
        diesel++;
}
while(entrada != 4);
```
###### Note que, como as condicionais possuem apenas uma linha dentro de cada, podemos omitir as chaves `{}`. Em códigos maiores, esta sintaxe não é recomendada.

_E se digitarem um código inválido, como um `5`? O que fazemos?_  
A resposta é: **nada**.  
Como os combustíveis só são alterados se o código deles for correspondente (1, 2 ou 3), não alteramos nada. O laço só é interrompido quando é digitado oum `4`, logo, vamos apenas ler o próximo valor até ser digitado um código válido.  

Por fim, após lermos todos os números, vamos exibir na tela a quantidade de clientes para cada tipo de combustível. Para facilitar a leitura, dividimos as linhas em 4 funções `printf()`. Primeiro o `MUITO OBRIGADO` que o exercício pede, em seguida a quantidade de clientes que abasteceram álcool, gasolina e diesel, sempre pulando uma linha no final com `\n`.

```c
printf("MUITO OBRIGADO\n");
printf("Alcool: %d\n", alcool);
printf("Gasolina: %d\n", gasolina);
printf("Diesel: %d\n", diesel);
```

##### Para revisar a estrutura de repetição: [Comando do while](http://linguagemc.com.br/comando-do-while/)
##### Para relembrar sobre condicionais: [Estruturas de decisão encadeadas](http://linguagemc.com.br/estruturas-de-decisao-encadeadas-if-else-if-else/)
    
Caso tenha alguma dúvida sobre este problema ou sobre a resolução, entre em contato com o PET-BCC pelo nosso
[Facebook](https://www.facebook.com/petbcc/),
[Instagram](https://www.instagram.com/petbcc.ufscar/)
ou nos mande um e-mail com o assunto "URI" para  petbcc.ufscar@gmail.com
