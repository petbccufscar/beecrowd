# Problema:
 
Faça um programa que leia o nome de um vendedor, o seu salário fixo e o total de vendas efetuadas por ele no mês (em dinheiro). Sabendo que este vendedor ganha 15% de comissão sobre suas vendas efetuadas, informar o total a receber no final do mês, com duas casas decimais.
 
##### Link do problema: https://www.urionlinejudge.com.br/judge/pt/problems/view/1009
 
# Resolução:
 
No enunciado do problema, está escrito para ler três valores: nome, salário e vendas. Após isso imprimir o total final.
 
Como a primeira variável é um nome devemos instanciá-la como um vetor de `char`:
 
```c
        char nome[]="";
```
 
As próximas variáveis por se tratarem de números decimais serão instanciadas como tipo `float`:
 
```c
        float salario, vendas, salariofinal; 
``` 
 
Para ler as variáveis, usa-se `scanf`:
 
```c
        scanf("%s %f %f", nome, &salario, &vendas);
```
 
É possível inserir mais de um dado dentro de um mesmo `scanf` separando os `%(variável)`, lembrando que a ordem das variáveis inseridas no `" "` deve corresponder com a ordem dos endereços de memória indicados na função. Durante a execução do programa, usamos `.` para separar o valor decimal do inteiro.
 
Obs: Como `nome` é um vetor seu nome já é seu endereço de memória, assim não se utiliza o `&` no `scanf`.
 
Em seguida, atribuímos o valor final. O enunciado diz que o salário final é a soma do salário do vendedor com 15% de comissão sobre suas vendas efetuadas, sendo assim:
 
```c
        salariofinal = salario + (vendas * 0.15f);
```
 
Para que a multiplicação fique computacionalmente correta devemos inserir o `f` ao final do `0.15` para que a constante seja declarada como float (32 bits), ao invés de double.
 
 
Assim, terminamos escrevemos o resultado na tela utilizando a função `printf`:
 
```c
        printf("TOTAL = R$ %.2f\n", salariofinal);
```
 
O `%0.2lf` será substituído pelo valor contido em `salariofinal`. O `.2` indica quantas casas decimais serão mostradas na tela, que no caso são duas.
 
##### Para revisar sobre variáveis: [Variáveis](http://linguagemc.com.br/variaveis-em-linguagem-c/)
 
##### Para revisar sobre tipos de variáveis: [Tipos de Variáveis](http://linguagemc.com.br/tipos-de-dados-em-c/)
 
##### Para aprender um pouco mais sobre vetor de caracteres: [String](http://linguagemc.com.br/string-em-c-vetor-de-caracteres/)
 
Caso tenha alguma dúvida sobre este problema ou sobre a resolução, entre em contato com o PET-BCC (facebook, twitter, etc)
 
