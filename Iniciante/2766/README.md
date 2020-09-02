# Problema:   
O seu professor gostaria de fazer um programa com as seguintes características:

1. Leia 10 nomes, sem espaço em branco;
2. Imprima o terceiro nome da lista;
3. Imprima o sétimo nome da lista;
4. Imprima o nono nome da lista.

**Problema Completo**: https://www.urionlinejudge.com.br/judge/pt/problems/view/2766

# Resolução:

Iniciaremos a resolução deste problema declarando as variaveis que iremos utilizar, serão 1 variavel do tipo inteiro a qual iremos utilizar em nosso laço de repetição `for` e uma variavel do tipo "char" na qual iremos armazenar, a cada iteração, uma palavra.
```c
int i;
char palavra[40];
```

Iremos realizar um total de 10 iterações variando o valor de i de "1" até "10", a cada iteração iremos realizar a leitura da palavra que iremos receber como entrada
```c
for (i = 1; i <= 10; i++){
	scanf("%s", palavra);
	...
}
```

Ainda dentro de nosso laço `for` após ler a palavra, verificamos se a iteração que estamos possui como indice "3", "7" ou "9", caso positivo para alguma desses condições, realizamos a impressão desta palavra na tela.
```c
if (i == 3 || i == 7 || i == 9)
	printf("%s\n", palavra);
```
    
Caso tenha alguma dúvida sobre este problema ou sobre a resolução, entre em contato com o PET-BCC pelo nosso
[Facebook](https://www.facebook.com/petbcc/),
[Instagram](https://www.instagram.com/petbcc.ufscar/)
ou nos mande um e-mail com o assunto "URI" para  petbcc.ufscar@gmail.com