# Problema:

Imprima os N primeiros caracteres da citação de Søren Kierkegaard definida pelas letras que foram sublinhadas no enunciado deste problema.

**Problema completo:** https://www.urionlinejudge.com.br/judge/pt/problems/view/1864

# Resoluçāo:

O exercício pede para imprimir na tela os N primeiros caracteres da frase da citaçāo de Søren, 'LIFE IS NOT A PROBLEM TO BE SOLVED'.

Primeiramente iremos declarar as seguintes variáveis `str`, `n` e `i`. A variável `i` é utilizada para iterar em um loop, `n` é a entrada que é digitada pelo usuário e `str` guarda a frase do problema.

```c
char str[34] = "LIFE IS NOT A PROBLEM TO BE SOLVED";
int n, i;
```

Em seguida, faremos a leitura do valor de `n`.

```c
scanf("%d",&n);
```

Após a leitura de `n`, utilizados o `for` para percorrer a frase e imprimindo um caracter por vez até a condiçāo de parada.

```c
    for(i=0;i<n;i++){
        printf("%c",str[i]);
    }
    printf("\n");
```

Ao termino do `for` é impresso a nova linha para que nāo ocorra erro de apresentaçāo.
 
##### Para aprender um pouco mais sobre o laço de repetição for: [For](http://linguagemc.com.br/a-estrutura-de-repeticao-for-em-c/)
 
##### Para aprender um pouco mais sobre caracteres: [Caracteres](http://linguagemc.com.br/string-em-c-vetor-de-caracteres/)

 
Caso tenha alguma dúvida sobre este problema ou sobre a resolução, entre em contato com o PET-BCC pelo nosso
[Facebook](https://www.facebook.com/petbcc/), [Instagram](https://www.instagram.com/petbcc.ufscar/), ou nos mande um e-mail com o assunto "URI" para  petbcc.ufscar@gmail.com