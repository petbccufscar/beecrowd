# Problema:   
O seu professor gostaria de fazer um programa com as seguintes características:

1. Leia 10 nomes, sem espaço em branco;
2. Imprima o terceiro nome da lista;
3. Imprima o sétimo nome da lista;
4. Imprima o nono nome da lista.

**Problema Completo**: https://www.urionlinejudge.com.br/judge/pt/problems/view/2766

# Resolução:

Iniciaremos a resolução deste problema declarando as 2 variáveis que iremos utilizar: `i`, do tipo inteiro, para utilizar no laço de repetição `for`; e `palavra`, do tipo `char`, na qual será armazenada, a cada iteração, uma palavra diferente e com tamanho máximo igual a 30.
```c
int i;
char palavra[30];
```

Iremos incrementar `i` até 10 (número máximo de linhas do arquivo), para que possamos realizar um total de 10 iterações. Em cada uma destas, faremos a leitura da palavra fornecida como entrada.
```c
for (i = 1; i <= 10; i++){
	scanf("%s", palavra);
	...
}
```

Em seguida, ainda dentro de nosso laço `for`, verificamos se a iteração atual possui índice "3", "7" ou "9". Caso positivo para alguma desses condições, a estrutura `if` garante que seja realizada a impressão de `palavra` na tela.
```c
if (i == 3 || i == 7 || i == 9)
	printf("%s\n", palavra);
```
    
Caso tenha alguma dúvida sobre este problema ou sobre a resolução, entre em contato com o PET-BCC pelo nosso
[Facebook](https://www.facebook.com/petbcc/),
[Instagram](https://www.instagram.com/petbcc.ufscar/)
ou nos mande um e-mail com o assunto "URI" para  petbcc.ufscar@gmail.com
