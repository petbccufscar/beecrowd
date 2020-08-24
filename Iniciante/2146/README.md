# Problema

Sr. Amnésio tinha uma grande dificuldade em guardar senhas. Para lembrá-las, ele sempre usava números, e as escrevia em pedaços de papel, que também perdia com facilidade, fazendo com que ele precisasse modificar a senha cada vez que isto acontecia. Cansado, ele pensou em uma forma mais prática: colocava no papel um número próximo da senha, depois ele usava sempre uma mesma conta para lembrar a senha, baseada no número escrito no papel. Mas ele também esquecia a fórmula, por isto, pediu para você escrever um programa que, dado o número do papel, informe a senha correspondente.

Escreva um programa que, dado um número, informe a respectiva senha.

##### Link do problema: https://www.urionlinejudge.com.br/judge/pt/problems/view/2146

# Resolução 

Para resolver o problema, enquanto a entrada não for End Of File (`EOF`), iremos ler a senha e exibi-lá conforme o padrão de saída exibido no problema.

Começamos incluindo a biblioteca `string.h`, que contém a terminologia de `EOF`.
```c
	#include <string.h>
```

Depois, declaramos a variável que será utilizada para armazenar a senha.
```c
	int senha;
```

Em seguida, iremos declarar nossa estrutura de repetição `while`. O critério de parada será a leitura (feita pela estrutura `scanf`) de um EOF.
```c
	while(scanf("%d", &senha) != EOF){
```

Enquanto a entrada não for EOF, iremos exibir a senha correta com a estrutura `printf`. Visto pelo padrão de entrada e saída exibido no exercício, vemos que a senha verdadeira é a senha inserida -1.
```c
    printf("%d\n", (senha-1));
```

Caso tenha alguma dúvida sobre este problema ou sobre a resolução, entre em contato com o PET-BCC pelo nosso
[Facebook](https://www.facebook.com/petbcc/),
[Instagram](https://www.instagram.com/petbcc.ufscar/)
ou nos mande um e-mail com o assunto "URI" para  petbcc.ufscar@gmail.com