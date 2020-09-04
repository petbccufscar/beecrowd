# Problema:

O seu professor de programação gostaria que você fizesse um programa com as seguintes características:

1. Crie vinte e seis variáveis inteira;
2. Atribua a primeira variável o valor 97;
3. Atribua as outras demais variável o valor da primeira somado de uma unidade;
4. Mostre na tela os valores numéricos da primeira variável, um espaço em braco, o carácter 'e', outro espaço em branco e o seu valor alfanumérico (caracteres);
5. Repita o procedimento para todas as outras variáveis.

###### Problema completo: https://www.urionlinejudge.com.br/judge/pt/problems/view/2753

# Resolução:

O objetivo deste problema é mostrar que a liguagem C representa as 26 letras do alfabeto com números. Isto é feito através da [Tabela ASCII](https://www.tecmundo.com.br/imagem/1518-o-que-e-codigo-ascii.htm).

Para iniciar o problema declaramos a variável `i`, que será utilizada para mostrar um número e seu caractere correspondente em ASCII.
```c
int i;
```

Por fim, criamos um laço de repetição `for`, que será percorrido 26 vezes, exibindo um número e seu caractere correspondente com o `printf`. Utilizamos o parâmetro `%c` no `printf`, pois ele que irá interpretar o número `i` como uma letra. Por exemplo, quando `i = 98` o comando `printf` exibirá a letra `b` no lugar do parâmetro `%c`.
```c
for(i=97; i <= 122 ; i++){

		printf("%d e %c\n", i, i);
}
```

Caso tenha alguma dúvida sobre este problema ou sobre a resolução, entre em contato com o PET-BCC pelo nosso
 * [Facebook](https://www.facebook.com/petbcc/),
 * [Instagram](https://www.instagram.com/petbcc.ufscar/)
 * ou nos mande um e-mail com o assunto "URI" para  petbcc.ufscar@gmail.com