# Problema:   
O seu professor gostaria de fazer um programa com as seguintes características:

1. Leia uma frase que vai ter uma virgula no meio do texto;
2. Imprima a primeira parte da frase;
3. Imprima a segunda parte da frase.

**Problema Completo**: https://www.urionlinejudge.com.br/judge/pt/problems/view/2765

# Resolução:

Iniciaremos a resolução deste problema declarando as variaveis que iremos utilizar, serão 2 variaveis "char" `primeira` e `segunda` onde iremos armazenar, respectivamente, a primeira parte a segunda parte da frase que iremos receber como entrada
```c
char primeira[100];
char segunda[100];
```

Iremos realizar a leitura da frase de outra maneira, utilizando os delimitadores `%[^,],%[^\n]`:
- `%[^,],` percorre a entrada até encontrar uma virgula e salva na variavel `primeira`, ao colocar a virgula após fechar o colchetes, irá descartar a virgula, armazenando apenas as letras.
- `%[^\n]` percorre até encontrar um `\n` que indica o final da frase e armazena o conteudo em nossa variavel `segunda`.
```c
scanf("%[^,],%[^\n]", &primeira, &segunda);
```

Ao final, imprimimos a primeira parte da frase sem considerar a virgula, e na linha de baixo a segunda parte da frase.
```c
printf("%s\n", primeira);
printf("%s\n", segunda);
```


##### Para revisar sobre: [função scanf](https://www.cprogramming.com/tips/tip/the-power-of-scanf)
    
Caso tenha alguma dúvida sobre este problema ou sobre a resolução, entre em contato com o PET-BCC pelo nosso
[Facebook](https://www.facebook.com/petbcc/),
[Instagram](https://www.instagram.com/petbcc.ufscar/)
ou nos mande um e-mail com o assunto "URI" para  petbcc.ufscar@gmail.com