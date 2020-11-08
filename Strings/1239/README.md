
# Problema: 1239  

Você está ajudando a desenvolver um sistema de gerenciamento de weblog chamado bloggo. Embora bloggo coloque todo o conteúdo direto no website em HTML, nem todos autores apreciam usar tags HTML em seus textos. Para tornar a vida deles mais fáceis, bloggo oferece uma sintaxe simples chamada atalhos para obter alguns efeitos textuais em HTML. Sua tarefa é, dado um documento escrito com atalhos, traduzi-lo para o HTML apropriado.


Um atalho é usado para colocar texto em itálico. HTML faz isto com as tags `<i>` e `</i>`, mas no bloggo um autor pode simplesmente colocar um pedaço de texto entre dois caracteres de sublinhado, '\_'. Portanto, onde um autor escreve

`You _should_ see the baby elephant at the zoo!`


bloggo vai publicar o seguinte:

`You <i>should</i> see the baby elephant at the zoo!`


Outro atalho serve para colocar texto em negrito, o que, em HTML, é feito com as tags `<b>` e `</b>`. Bloggo permite aos autores fazer o mesmo com pares do caractere asterisco, '\*'. Quando um autor escreve o texto

`Move it from *Receiving* to *Accounts Payable*.`


ele vai sair no website assim:

`Move it from <b>Receiving</b> to <b>Accounts Payable</b>.`

**Problema Completo**: https://www.urionlinejudge.com.br/judge/pt/problems/view/1239

# Resolução:

O exercício pede para substituir pares de caracteres '\*' e '\_',  presentes no texto da entrada, pelas tags em [*Hypertext Markup Language* (HTML)](https://developer.mozilla.org/pt-BR/docs/Web/HTML) `<b></b>` e `<i></i>` , sendo que o texto posicionado entre estas tags recebe um efeito de negrito ou itálico, respectivamente. Cada caso de teste é recebido na entrada em forma de uma linha de texto que possui caracteres normais e os caracteres a serem substituídos. Os casos de teste acabam quando for identificado o fim entrada, representado pela constante `EOF`. Para cada linha de texto recebida, deve-se fornecer o resultado correspondente com a substituição dos caracteres '\*' e '\_' pelas tags HTML.

 De acordo com a especificação fornecida pelo exercício, existem certas pressuposições que devem ser consideradas acerca dos caracteres que compoẽm cada linha da entrada:

1. "O caractere sublinhado '\_' ocorre no texto um número par de vezes. O asterisco '\*' também aparece um número par de vezes no texto."

2. "Nenhuma substring do texto entre um par de sublinhados ou entre um par de asteriscos pode conter outros sublinhados ou asteriscos, respectivamente."

3. "Os únicos caracteres permitidos no texto são os caracteres alfabéticos (de 'a' a 'z' e de 'A' a 'Z'), o sublinhado ('\_'), o asterisco ('\*'), o caractere de espaço e os símbolos de pontuação ',', ';', '.', '!', '?', '-', '(' e ')'."

O exercício não especifica se as pressuposições 1, 2 e 3 são restrições que devem ser tratadas pela lógica do programa, uma vez que não há nenhuma orientação de como tratá-las na saída do programa. Dessa maneira, é razoável assumir que a entrada a ser recebida já irá cumprir tais restrições, sem a necessidade de validação das linhas de entrada por parte do programa.

Utilizamos uma variável do tipo caractere para armazenar cada caractere lido na entrada, uma variável inteira para indicar que um primeiro asterisco referente a um par de asteriscos foi encontrado e uma variável inteira para indicar que um primeiro sublinhado referente a um par de sublinhados foi encontrado.

```c
char caractere;
int encontrado_negrito, encontrado_italico;
```
Inicialmente, atribui-se valor zero às variáveis  `encontrado_negrito` e `encontrado_italico`, significando que ainda não foi encontrado o primeiro asterisco referente a um par de asteriscos. Precisamos dessa informação para determinar qual tag deve ser mostrada na saída (`</b>`, `</i>` ou `<b>`, `<i>`).

```c
encontrado_negrito = 0;
encontrado_italico = 0;
```

Para a leitura da entrada, utilizamos um laço `while` com a função `scanf`
para ler cada caractere da entrada e armazená-lo na variável `caractere`. A constante `EOF` pertence à biblioteca `stdio.h`, assume valor -1 na maioria dos computadores e indica o fim da entrada dos dados. Com isso, o programa sairá do laço quando a função `scanf` retornar o valor `EOF`.

##### Para aprender um pouco mais sobre entrada e saída: [Entrada e saída](https://www.ime.usp.br/~pf/algoritmos/aulas/io.html)

```c
while(scanf("%c", &caractere) != EOF){
```

Posteriormente, verificamos se o caractere lido é igual ao caractere asterisco através de um `if`. Caso esta condição seja verdade temos outras duas verificações feitas sobre o valor da variável `encontrado_negrito`. Há um `ìf` que verifica se `encontrado_negrito` possui valor 0. Isso indica que até o momento não foi encontrado outro asterisco.

 Já que o caractere analisado é um asterisco e o primeiro encontrado, utilizamos a função `print` para enviar a tag `<b>`para a posição respectiva da saída.  Além disso, alteramos o valor da variável `encontrado_negrito` para 1, indicando que foi encontrado o primeiro par de asteriscos. Essa indicação permite que seja possível identificar  que o próximo asterisco que for encontrado corresponde ao segundo asterisco daquele par, o que permite colocar a tag `</b>` na saída.

Dessa forma, há também uma verificação por meio do `else if` que analisa se `encontrado_negrito` é igual a 1,  colocando `</b>` na saída e alterando o valor de `encontrado_negrito` para 0 novamente. Com isso, torna-se possível diferenciar os momentos de colocarmos ou `<b>` ou `</b>` na saída.

 ```c
   if(caractere == '*'){
     if(encontrado_negrito == 0){
       printf("<b>");
       encontrado_negrito = 1;
     }
     else if(encontrado_negrito == 1){
       printf("</b>");
       encontrado_negrito = 0;
     }
   }
 ```

 De maneira semelhante, também verificamos se o caractere que foi lido é igual ao sublinhado, através do `else if`. Dentro deste `else if` temos outras duas estruturas condicionais (`if` e `else if`) que analisam se a variável `encontrado_italico` possui o valor 1 ou 0, indicando que o primeiro sublinhado referente a um par de sublinhados foi encontrado ou não, respectivamente. Com essas verificações, coloca-se na saída o caractere `<b>` ou `</b>` e altera-se o valor da variável `encontrado_italico` para _1_ ou _0._
 0.

 ```c
   else if(caractere == '_'){
     if(encontrado_italico == 0){
       printf("<i>");
       encontrado_italico = 1;
     }
     else if(encontrado_italico == 1){
       printf("</i>");
       encontrado_italico = 0;
     }
   }
 ```
Por fim, caso o caractere lido e armazenado na variável `caractere` não seja nem um asterisco, nem um sublinhado, o programa entra no `else` que possui apenas um comando `print` para colocar este caractere na saída.

```c
  else{
    printf("%c", caractere);
  }
}
```
Caso tenha alguma dúvida sobre este problema ou sobre a resolução, entre em contato com o PET-BCC pelo nosso
[Facebook](https://www.facebook.com/petbcc/),
[Instagram](https://www.instagram.com/petbcc.ufscar/)
ou nos mande um e-mail com o assunto "URI" para  petbcc.ufscar@gmail.com
