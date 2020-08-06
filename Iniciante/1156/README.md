# Problema:    
Escreva um algoritmo para calcular e escrever o valor de S, sendo S dado pela fórmula:
S = 1 + 3/2 + 5/4 + 7/8 + ... + 39/?

**Problema completo**: https://www.urionlinejudge.com.br/judge/pt/problems/view/1156


# Resolução:
Para resolver o exercício, o primeiro passo é entender a fórmula fornecida:

- S = 1 + 3/2 + 5/4 + 7/8 + ... + 39/?  equivale a:

- S = n/i⁰ + n+2/i¹ + n+4/i² + … + 39/? , com o valor inicial de n = 1, valor final de n = 39 e valor de i = 2;

O segundo passo é declarar as variáveis necessárias para o problema:

```c
double soma = 0, numerador = 1, n = 2, i = 0;
```
 
Em seguida, vamos utilizar um loop `while` que será executado enquanto `n <= 39`. Vamos utilizar a seguinte lógica:  

- Adiciona-se a divisão do numerador pela potência de 2 elevado a i, `numerador/pow(n, i)` a `soma`;
- Incrementa-se `numerador` em 2;
- Incrementa-se `i` em 1.


```c
while (numerador <= 39) {
        
        soma += numerador/pow(n, i);

        numerador += 2;
        i++;
}
```

Fora do laço, imprimi-se a `soma` com duas casas decimais e com a quebra de linha `\n`.

```c    
printf("%.2f\n", soma);
```

##### Para revisar sobre o laço while: [O comando while](http://linguagemc.com.br/o-comando-while-em-c/)
    
Caso tenha alguma dúvida sobre este problema ou sobre a resolução, entre em contato com o PET-BCC pelo nosso
[Facebook](https://www.facebook.com/petbcc/),
[Instagram](https://www.instagram.com/petbcc.ufscar/)
ou nos mande um e-mail com o assunto "URI" para  petbcc.ufscar@gmail.com
