# Problema:
O seu professor gostaria de fazer um programa com as seguintes características:

1. Leia um número no formato: XXXXX.YYY;
2. Imprima o número na forma invertida: YYY.XXXXX.

**Problema Completo**: https://www.urionlinejudge.com.br/judge/pt/problems/view/2762


# Resolução:
O ponto chave do exercício consiste em armazenar a entrada de modo a admitir seu acesso em partes. Para isto, primeiramente, declaramos as variáveis inteiras `X` e `Y`.  

```c
int X, Y;
```  

Em seguida, podemos realizar a leitura dos dados: utilizamos `X` para guardar a parte inteira do valor fornecido, enquanto `Y` guardará a parte decimal. Como a entrada terá um ponto entre estes dois números, o inserimos diretamente na função `scanf()`.  

```c
scanf("%d.%d", &X, &Y);
```  

Agora, basta que `printf()` exiba os valores em ordem invertida, mantendo o ponto ao meio.  

```c
printf("%d.%d\n", Y, X);
```  


Caso tenha alguma dúvida sobre este problema ou sobre a resolução, entre em contato com o PET-BCC pelo nosso [Facebook](https://www.facebook.com/petbcc/), [Instagram](https://www.instagram.com/petbcc.ufscar/) ou nos mande um e-mail com o assunto "URI" para  petbcc.ufscar@gmail.com
