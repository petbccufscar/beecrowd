# Problema: 

O seu professor de programação gostaria que você fizesse um programa com as seguintes características:

1. Crie uma variável para armazenar 50 caracteres;
2. Atribua a variável anterior a frase: "AMO FAZER EXERCICIO NO URI";
3. Mostre na primeira linha o carácter <, o valor armazenado na variável com o formato "%s" e o carácter >;
4. Mostre na linha seguinte o carácter < , o valor armazenado na variável com o formato "%30s" e o carácter >;
5. Mostre na linha seguinte o carácter < , o valor armazenado na variável com o formato "%.20s" e o carácter >;
6. Mostre na linha seguinte o carácter < , o valor armazenado na variável com o formato "%-20s" e o carácter >;
7. Mostre na linha seguinte o carácter < , o valor armazenado na variável com o formato "%-30s" e o carácter >;
8. Mostre na linha seguinte o carácter < , o valor armazenado na variável com o formato "%.30s" e o carácter >;
9. Mostre na linha seguinte o carácter < , o valor armazenado na variável com o formato "%30.20s" e o carácter >;
10. Mostre na linha seguinte o carácter < , o valor armazenado na variável com o formato "%-30.20s" e o carácter >;

###### Problema completo: https://www.urionlinejudge.com.br/judge/pt/problems/view/2752

# Resolução:

O objetivo deste exercício consiste em realizar a exibição de um vetor de caracteres de diversas formas, através do comando `printf`.

Para começar declaramos a única variável do problema: `frase`, que é um vetor de caracteres e irá armazenar a frase a ser exibida de diversas formas com o `printf`.
```c
char frase[50] = "AMO FAZER EXERCICIO NO URI";
```
Note que, ao ser iniciado, o vetor recebe a frase "AMO FAZER EXERCICIO DE URI", que possui 26 caracteres.

Depois, podemos realizar todas as impressões com as características listadas no problema:

3. Com o parâmetro `%s` no comando `printf` exibimos todo o conteúdo do vetor ("AMO FAZER EXERCICIO DE URI").
```c
printf("<%s>\n", frase);
```

4. Com o parâmetro `%30s` no comando `printf` exibimos todo o conteúdo do vetor mais alguns espaços, a esquerda, até ele ter `30` caracteres ("    AMO FAZER EXERCICIO NO URI").
```c
printf("<%30s>\n", frase);
```

5. Com o parâmetro `%.20s` exibimos o conteúdo do vetor com apenas `20` caracteres ("AMO FAZER EXERCICIO ").
```c
printf("<%.20s>\n", frase);
```

6. Com o parâmetro `%-20s`, `frase` é exibida normalmente, pois esse parâmetro funciona apenas se o tamanho do vetor for menor que 20 caracteres. Se fosse o caso, serviria para acrescentar espaços a direita do vetor até completar `20` caracteres (AMO FAZER EXERCICIO NO URI).
```c
printf("<%-20s>\n", frase);
```

7. O parâmetro `%-30s` funciona exatamente como o anterior, mas dessa vez irá exibir o vetor e mais alguns espaços a direita, pois o tamanho de `frase` é menor que `30` caracteres (AMO FAZER EXERCICIO NO URI    ).
```c
    printf("<%-30s>\n", frase);
```

8. O parâmetro `%.30s` funciona igual ao `%.20s` (característica 5), mas irá exibir o vetor todo pois ele é menor que 30 caracteres (AMO FAZER EXERCICIO NO URI). 
```c  
printf("<%.30s>\n", frase);
```

9. O parâmetro `%30.20s` é uma junção das características 4 e 5, dessa forma `frase` será exibida com o tamanho de 20 caracteres e com um espaçamento a esquerda até possuir 30 caracteres ("          AMO FAZER EXERCICIO ").
```c
printf("<%30.20s>\n", frase);
```

10. O parâmetro `%-30.20s` é uma junção das características 5 e 7, dessa forma `frase` será exibida com o tamanho de 20 caracteres e com um espaçamento a direita até possuir 30 caracteres ("AMO FAZER EXERCICIO           ").
```c
    printf("<%-30.20s>\n", frase);
```

##### Para aprender um pouco mais sobre saída de dados e formatação de texto com `printf` : [printf](https://programacaopratica.com.br/2019/09/17/entendendo-a-funcao-printf-da-linguagem-c/)

Caso tenha alguma dúvida sobre este problema ou sobre a resolução, entre em contato com o PET-BCC pelo nosso
 * [Facebook](https://www.facebook.com/petbcc/),
 * [Instagram](https://www.instagram.com/petbcc.ufscar/)
 * ou nos mande um e-mail com o assunto "URI" para  petbcc.ufscar@gmail.com
