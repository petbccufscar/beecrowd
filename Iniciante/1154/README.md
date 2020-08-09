# Problema:    
Faça um algoritmo para ler um número indeterminado de dados, contendo cada um, a idade de um indivíduo. O último dado, que não entrará nos cálculos, contém o valor de idade negativa. Calcular e imprimir a idade média deste grupo de indivíduos.

**Problema completo**: https://www.urionlinejudge.com.br/judge/pt/problems/view/1154


# Resolução:
Para resolver o exercício, o primeiro passo é declarar as variáveis necessárias para o problema: `idade`, `n` e `soma`. Iremos utilizar `n` para contar quantos números foram lidos e `soma` para armazenar a soma de todas as idades lidas, por conta disso, as duas são iniciadas com 0. Vale notar que `soma` é declarado como `double` pois o exercício informa que a média deve ser impressa com dois dígitos após o ponto decimal.

```c
int idade, n = 0;
double soma = 0;
```

Em seguida, faremos a leitura do valor `idade`.

```c
scanf("%d", &idade);
```

Para ler um número indeterminado de dados, vamos utilizar um loop `while` que será executado enquanto `idade >= 0`. Vamos utilizar a seguinte lógica:  

- A `idade` lida é adicionada a soma de todas as idades (`soma`);
- Incrementa-se 1 ao contador de números lidos (`n`).

Ao final, devemos ler o número `idade` para a próxima execução do `while`, utilizando novamente a função `scanf`.

```c
while (idade >= 0) {
        
    soma += idade;
    n++;
    scanf("%d", &idade);
}
```

Fora do laço, imprimi-se o cálculo da média, que é `soma/n` com duas casas decimais e com a quebra de linha `\n`.

```c    
printf("%.2f\n", soma/n);
```

##### Para revisar sobre o laço while: [O comando while](http://linguagemc.com.br/o-comando-while-em-c/)
    
Caso tenha alguma dúvida sobre este problema ou sobre a resolução, entre em contato com o PET-BCC pelo nosso
[Facebook](https://www.facebook.com/petbcc/),
[Instagram](https://www.instagram.com/petbcc.ufscar/)
ou nos mande um e-mail com o assunto "URI" para  petbcc.ufscar@gmail.com
