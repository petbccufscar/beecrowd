# Problema:
 
Leia um valor inteiro *N*. Este valor será a quantidade de valores inteiros *X* que serão lidos em seguida.
Mostre quantos destes valores *X* estão dentro do intervalo [10,20] e quantos estão fora do intervalo, mostrando essas informações.
 
##### Link do problema: https://www.urionlinejudge.com.br/judge/pt/problems/view/1072
 
# Resolução:
 
Primeiro vamos instanciar as variaveis necessarias, vamos precisar de um cinco valores inteiros, sendo eles para contar os valores dentro e fora do intervalo, contador do `for()`, o valor *N* a ser lido e o valores de *X*.
 
 
```c
int cont, n, x, dentro=0, fora=0;
```
 
Lemos o valor de *N*.
 
```c
scanf("%d", &n);
```
Agora iremos utilizar o `for()` para analisar cada `valor` de *X* separadamente. Dentro dele iremos ler um valor de *X* e verificar se ele está dentro do intervalo ou não utilizando `if` e `else`, caso seja verdadeiro adicionamos 1 a variável *dentro*, caso contrário adicionamos na variável *fora*.
 
```c
for(cont=1; cont<=n; cont++){
    scanf("%d", &valor);
    if(valor>=10 && valor<=20)
        dentro++;
    else
        fora++;
}
```
 
Por fim imprimimos na tela quantos estão dentro do intervalo e quantos estão fora.
```c
printf("%d in\n", dentro);
printf("%d out\n", fora);
```
 
##### Para aprender um pouco mais sobre o laço de repetição for: [For](http://linguagemc.com.br/a-estrutura-de-repeticao-for-em-c/)
 
Caso tenha alguma dúvida sobre este problema ou sobre a resolução, entre em contato com o PET-BCC pelo nosso
[Facebook](https://www.facebook.com/petbcc/),
[Instagram](https://www.instagram.com/petbcc.ufscar/)
ou nos mande um e-mail com o assunto "URI" para  petbcc.ufscar@gmail.com
 


