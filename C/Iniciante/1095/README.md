# Problema:
Você deve fazer um programa que apresente a sequencia conforme o exemplo abaixo.

Conforme esclarecido pelo exercício, "não há nenhuma entrada neste problema" e deve-se imprimir "a sequencia conforme exemplo".

**Problema Completo**: https://www.urionlinejudge.com.br/judge/pt/problems/view/1095


# Resolução:
O exercício resume-se a decifrar o padrão da sequência exemplificada e, então, exibir todos os valores obtidos até que *J=0*. Analisando os valores fornecidos, é possível notar que I é incrementado em 3, enquanto J é decrementado em 5.  

Como o primeiro valor de ambos já é disponibilizado, podemos declarar as variáveis inteiras `I` e `J` inicializando-as, respectivamente, com 1 e 60.  

```c
int I=1;
int J=60;
```

Visto que o programa deve encerrar-se após `J` atingir valor equivalente a 0 (incluindo-o), é vantajoso utilizarmos a estrutura de repetição `while` para que o incremento/decremento seja feito **enquanto** `J` armazenar um número maior ou igual a 0.
No interior da estrutura, realizamos, primeiramente, a exibição dos valores iniciais das variáveis (através da função `printf()`) e, em seguida, podem ser feitas as operações de soma e subtração das mesmas. Assim, seus valores serão modificados e expostos na tela a cada iteração, até que a condição imposta seja alcançada.  

```c
while(J>=0){
  printf("I=%d J=%d\n",I,J);
  I = I + 3;
  J = J - 5;
}
```

##### Para aprender um pouco mais sobre a estrutura while: [O que é e como usar o laço WHILE](https://www.cprogressivo.net/2013/02/O-que-e-e-como-usar-o-laco-WHILE-em-C.html)  

Caso tenha alguma dúvida sobre este problema ou sobre a resolução, entre em contato com o PET-BCC pelo nosso [Facebook](https://www.facebook.com/petbcc/), [Instagram](https://www.instagram.com/petbcc.ufscar/) ou nos mande um e-mail com o assunto "URI" para  petbcc.ufscar@gmail.com
