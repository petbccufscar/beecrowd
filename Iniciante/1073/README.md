# Problema:
 
Leia um valor inteiro *N*. Apresente o quadrado de cada um dos valores pares, de 1 até *N*, inclusive *N*, se for o caso.
 
##### Link do problema: https://www.urionlinejudge.com.br/judge/pt/problems/view/1073
 
# Resolução:
 
Primeiro instanciamos as variáveis necessárias, dois inteiros (um para o *N* e um para ser o contador do `for()`)
 
```c
    int num, cont;
```
 
Lemos o valor de *N*.
 
```c
    scanf("%d", &num);
```
 
Agora no `for()`, nós iniciaremos ele com `cont=2`, utilizaremos um `<=` para comparar *N* com o `cont` e por fim iremos incrementar o contador de 2 em 2 (`cont+=2`) para que ele sempre seja par.
Dentro do `for()` iremos imprimir o quadrado de cada par (sendo q o nosso par é o contador), assim, finalizando a lógica.
 
```c
    for ( cont = 2; cont <= num; cont+=2)
    {
        printf("%d^2 = %d\n", cont,(cont*cont));
    }
```
 
##### Para aprender um pouco mais sobre o laço de repetição for: [For](http://linguagemc.com.br/a-estrutura-de-repeticao-for-em-c/)
 
Caso tenha alguma dúvida sobre este problema ou sobre a resolução, entre em contato com o PET-BCC pelo nosso
[Facebook](https://www.facebook.com/petbcc/),
[Instagram](https://www.instagram.com/petbcc.ufscar/)
ou nos mande um e-mail com o assunto "URI" para  petbcc.ufscar@gmail.com
 

