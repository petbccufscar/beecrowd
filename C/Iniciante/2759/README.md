# Problema:

O seu professor gostaria de fazer um programa com as seguintes características:

    1. Crie 3 variáveis para armazenar um único carácter;
    2. Leia um valor carácter para a primeira variável;
    3. Leia um valor carácter para a segunda variável;
    4. Leia um valor carácter para a terceira variável;
    5. Imprima a letra A, um espaço em branco, o sinal de igual, um espaço em branco, o carácter armazenado na primeira variável lida no passo 2, uma virgula, um espaço em branco, a letra B, um espaço em branco, o sinal de igual, um espaço em branco, o carácter armazenado na segunda variável lida no passo 3, a letra C, um espaço em branco, o sinal de igual, um espaço em branco, o carácter armazenado na terceira variável lida no passo 4. Não esqueça de pular linha;
    6. Imprima a letra A, um espaço em branco, o sinal de igual, um espaço em branco, o carácter armazenado na primeira variável lida no passo 3, uma virgula, um espaço em branco, a letra B, um espaço em branco, o sinal de igual, um espaço em branco, o carácter armazenado na segunda variável lida no passo 4, a letra C, um espaço em branco, o sinal de igual, um espaço em branco, o carácter armazenado na terceira variável lida no passo 2. Não esqueça de pular linha;
    7. Imprima a letra A, um espaço em branco, o sinal de igual, um espaço em branco, o carácter armazenado na primeira variável lida no passo 4, uma virgula, um espaço em branco, a letra B, um espaço em branco, o sinal de igual, um espaço em branco, o carácter armazenado na segunda variável lida no passo 2, a letra C, um espaço em branco, o sinal de igual, um espaço em branco, o carácter armazenado na terceira variável lida no passo 3. Não esqueça de pular linha.

###### Problema completo: https://www.urionlinejudge.com.br/judge/pt/problems/view/2759

# Resolução:
Diferente da maioria dos exercícios do URI, o enunciado passa um algoritmo. Para o exercício, vamos seguir esse algoritmo passo a passo.

Começamos declarando três variáveis sendo elas `a`, `b` e `c` do tipo `char`: 
```c
  char a, b, c;
```
Essa parte representa o passo 1 do exercício. As etapas 2 a 4 pedem a leitura de cada uma dessas variáveis. Aqui usamos a função `scanf`:
```c
  scanf("%c %c %c", &a, &b, &c);
```
Podemos ler mais de uma variável dentro do mesmo `scanf` ao escrever mais de um `%c` entre as aspas.

O passo 5 pede para escrever os valores `a`, `b` e `c` lidos. Vamos usar o `printf`:
```c
  printf("A = %c, B = %c, C = %c\n", a, b, c);
```
Os passos 6 e 7 pedem o mesmo que o passo 5, mas em ordens diferentes. Na etapa 6 os valores irão aparecer na ordem `b`, `c` e `a`; na etapa 7 aparecerão na ordem `c`, `a` e `b`:
```c
  printf("A = %c, B = %c, C = %c\n", b, c, a);
  printf("A = %c, B = %c, C = %c\n", c, a, b);
```

Caso tenha alguma dúvida sobre este problema ou sobre a resolução, entre em contato com o PET-BCC pelo nosso
* [Facebook](https://www.facebook.com/petbcc/),
* [Instagram](https://www.instagram.com/petbcc.ufscar/)
* ou nos mande um e-mail com o assunto "URI" para  petbcc.ufscar@gmail.com


