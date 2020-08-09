# Problema:    
Escreva um algoritmo para calcular e escrever o valor de S, sendo S dado pela fórmula:
S = 1 + 1/2 + 1/3 + … + 1/100

**Problema completo**: https://www.urionlinejudge.com.br/judge/pt/problems/view/1155


# Resolução:
Para resolver o exercício, o primeiro passo é entender a fórmula fornecida:

- S = 1 + 1/2 + 1/3 + … + 1/100  equivale a:

- S = 1/n + 1/n + ... + 1/n em que o valor de n aumenta em 1 a cada fração somada, com o valor inicial de n = 1 e valor final de n = 100;

O segundo passo é declarar as variáveis necessárias para o problema:

```c
double soma = 0, n = 1;
```

Em seguida, vamos utilizar um loop `while` que será executado enquanto `n <= 100`. Vamos utilizar a seguinte lógica:  

- Adiciona-se `1/n` a `soma`;
- Incrementa-se 1 a `n`.

```c
while (n <= 100) {
        
        soma += 1/n;
        n++;

}
```

Fora do laço, imprimi-se a `soma` com duas casas decimais, e com a quebra de linha `\n`.

```c    
printf("%.2f\n", soma);
```

##### Para revisar sobre o laço while: [O comando while](http://linguagemc.com.br/o-comando-while-em-c/)
    
Caso tenha alguma dúvida sobre este problema ou sobre a resolução, entre em contato com o PET-BCC pelo nosso
[Facebook](https://www.facebook.com/petbcc/),
[Instagram](https://www.instagram.com/petbcc.ufscar/)
ou nos mande um e-mail com o assunto "URI" para  petbcc.ufscar@gmail.com
