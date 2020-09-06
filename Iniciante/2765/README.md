# Problema:   
O seu professor gostaria de fazer um programa com as seguintes características:

1. Leia uma frase que vai ter uma virgula no meio do texto;
2. Imprima a primeira parte da frase;
3. Imprima a segunda parte da frase.

**Problema Completo**: https://www.urionlinejudge.com.br/judge/pt/problems/view/2765

# Resolução:

Iniciaremos a resolução deste problema declarando as 2 variáveis do tipo `char` que iremos utilizar: `primeira` e `segunda`, onde armazenaremos, respectivamente, a 1ª e a 2ª parte da frase recebida como entrada.
```c
char primeira[100];
char segunda[100];
```

A leitura da frase será feita utilizando os delimitadores `%[^,]` e `%[^\n]`:
- `%[^,]` percorre a entrada (salvando seu conteúdo em `primeira`) até encontrar uma vírgula;
- `%[^\n]` percorre o restante da entrada (armazenando-a na variável `segunda`) até encontrar um `\n`, que indica o final da frase).  
Além disso, inserimos uma vírgula (,) entre os dois delimitadores para que esta seja descartada quando lida.
```c
scanf("%[^,],%[^\n]", &primeira, &segunda);
```

Ao final, imprimimos a primeira parte da frase (sem considerar a virgula) e, na linha abaixo, a segunda.
```c
printf("%s\n", primeira);
printf("%s\n", segunda);
```


##### Para revisar sobre: [função scanf](https://www.cprogramming.com/tips/tip/the-power-of-scanf)
    
Caso tenha alguma dúvida sobre este problema ou sobre a resolução, entre em contato com o PET-BCC pelo nosso
[Facebook](https://www.facebook.com/petbcc/),
[Instagram](https://www.instagram.com/petbcc.ufscar/)
ou nos mande um e-mail com o assunto "URI" para  petbcc.ufscar@gmail.com
