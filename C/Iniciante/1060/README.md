# Problema:

 Faça um programa que leia 6 valores. Estes valores serão somente negativos ou positivos (desconsidere os valores nulos). A seguir, mostre a quantidade de valores positivos digitados.

**Problema completo:** https://www.urionlinejudge.com.br/judge/pt/problems/view/1060

# Resolução:

Conforme o exemplo dado no exercício, os valores dados podem ser reais. Sendo assim, utilizaremos o tipo `float` para eles. Também utilizaremos uma variável inteira para contar quantos valores são positivos, que deve ser iniciada com 0.

```c
float valor;
int positivos = 0;
```

Faremos 6 leituras e verificamos se cada valor digitado é positivo. Caso seja, incrementamos a variável `positivos`.

```c
for(i = 0; i < 6; i++) {
    scanf("%f", &valor);

    if(valor > 0) {
        positivos++;
    }
}
```

Por fim, exibimos a quantidade de números positivos, sem esquecer de adicionar a quebra de linha (`\n`) ao final:

```c
printf("%d valores positivos\n", positivos);
```

##### Para aprender mais sobre [variáveis para números reais](https://www.cprogressivo.net/2012/12/Os-tipos-float-e-double-numeros-decimais-reais-em-C.html)

##### Para aprender mais sobre [operadores de incremento e decremento do C ](http://excript.com/linguagem-c/operador-incremento-decremento-c.html)

Caso tenha alguma dúvida sobre este problema ou sobre a resolução, entre em contato com o PET-BCC pelo nosso [Facebook](https://www.facebook.com/petbcc/),
[Instagram](https://www.instagram.com/petbcc.ufscar/)
ou nos mande um e-mail com o assunto "URI" para  petbcc.ufscar@gmail.com