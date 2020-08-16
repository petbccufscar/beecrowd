# Problema:    
Os cientistas da NASA descobriram um novo exoplaneta que fica a 1 bilhão de anos luz da terra. O nome desse planeta foi batizado de Pronalândia em homenagem aos novos cientistas que estão sendo formados no PRONATEC. Só que o mais incrível ainda está por vir. Ao observar melhor o planeta eles conseguiram identificar que os habitantes da Pronalândia estavam querendo se comunicar por uma numeração. Só que a numeração que encontraram está invertida e como encontraram muitas delas chamaram você para conseguir automatizar esse processo. Logo, dado um número grande, sua tarefa é imprimir esse número invertido.

**Problema completo**: https://www.urionlinejudge.com.br/judge/pt/problems/view/1984


# Resolução:
Devemos ler um número e exibi-lo ao contrário. O segredo deste tipo de exercício é tratar números como caracteres, assim podemos simplesmente percorrer os caracteres de trás para frente.  

Para isso, vamos precisar saber o número de caracteres (casas) que o valor tem. A função que retorna esse número está na biblioteca `<string.h>`, importada no início do código.

```c
#include <string.h>
```

Começaremos declarando duas variáveis:
- `numeros[10]` com 10 posições, já que os valores podem chegar até 10 casas (9999999999);
- um contador `i` para percorrer o vetor de caracteres.

```c
char numero[10];
int i;
```

Faremos a leitura do número - ou melhor, do vetor de caracteres.

```c
scanf("%s", numero);
```

Agora, vamos percorrer o vetor de trás para frente. Para descobrir quantas casas foram lidas e em qual posição iniciar, vamos utilizar a função `strlen` da biblioteca importada no início do código. Como essa função retorna o tamanho do vetor e os vetores começam sempre em 0, devemos iniciar nosso contador com uma posição a menos.  
Assim, percorremos todas as posições do final (`srtlen(numero) - 1`) até o início do vetor (`0`). Para cada posição, imprimimos o valor na tela.

```c
for (i = (strlen(numero) - 1); i >= 0; i--) {
    printf("%c", numero[i]);
}
```

Assim, terminamos de exibir o número ao contrário. O exercício nos lembra de pular uma linha ao final, o que é padrão para todo problema do URI.

```c
printf("\n");
```

##### Para relembrar sobre o laço for: [O comando for](http://linguagemc.com.br/a-estrutura-de-repeticao-for-em-c/)
##### Para revisar sobre vetores de caracteres: [String em C](http://linguagemc.com.br/string-em-c-vetor-de-caracteres/)
##### Para aprender mais sobre a biblioteca string.h: [A biblioteca string.h e suas funções ](https://www.cprogressivo.net/2013/03/Aprenda-a-usar-todas-as-funcoes-da-biblioteca-string-h-em-C.html)

Caso tenha alguma dúvida sobre este problema ou sobre a resolução, entre em contato com o PET-BCC pelo nosso
[Facebook](https://www.facebook.com/petbcc/),
[Instagram](https://www.instagram.com/petbcc.ufscar/)
ou nos mande um e-mail com o assunto "URI" para  petbcc.ufscar@gmail.com
