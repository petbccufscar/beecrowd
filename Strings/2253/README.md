# Problema:

Rolien e Naej são os desenvolvedores de um grande portal de programação. Para ajudar no novo sistema de cadastro do site, eles requisitaram a sua ajuda. Seu trabalho é fazer um código que valide as senhas que são cadastradas no portal, para isso você deve atentar aos requisitos a seguir:

- A senha deve conter, no mínimo, uma letra maiúscula, uma letra minúscula e um número;
- A mesma não pode ter nenhum caractere de pontuação, acentuação ou espaço;
- Além disso, a senha pode ter de 6 a 32 caracteres.

**Problema completo:** https://www.urionlinejudge.com.br/judge/pt/problems/view/2253

# Resoluçāo:

A ideia deste exercício é fazer verificações, de acordo com as especificações das senhas, a fim de achar algo que não pertença aos requisitos do validador de senhas. 

Primeiramente, vamos declarar a biblioteca `string.h` pois usaremos a função `gets` para poder ler a nossa entrada.

```c
    #include <string.h>
```

Então iremos declarar as variáveis inteiras e caracteres. Serão elas:
* `senha[255]`, variável para receber a senha a ser verificada;
* `i`, inteiro auxiliar para laços;
* `tam`, guardará o tamanho de `senha`
* `maiuscula`, terá 1 se existe pelo menos uma letra maiuscula em `senha`;
* `minuscula`, terá 1 se existe pelo menos uma letra minusculas em `senha`;
* `numero`, terá 1 se existir pelo menos um número em `senha`;
* `ehInvalida`, variável que recebe 1 caso a senha seja inválida;

```c
    char senha[255];
    int i, tam;
    int maiuscula, minuscula, numero, ehInvalida;
```

Então lemos a senha, usando a função `gets`, enquanto a entrada for diferente de `NULL`.

```c
 while (gets(senha) != NULL)
    {
        //Lógica do exercício
    }
```

Atribuímos todos os valores inteiros a 0 e guardamos o tamanho de `senha` em `tam`. Essa atribuição é importante para evitar valores errados.

```c
    ehInvalida = 0;
    numero = 0;
    maiuscula = 0;
    minuscula = 0;
    tam = strlen(senha);
```

Usando um `for` percorremos cada caractere da nossa entrada, verificando se algum caractere não está de acordo com os requisitos pedidos; usamos o número ASCII de cada caractere para isso. Estas condicionais verificam respectivamente os seguintes coisas:
* Se o caractere é um espaço;
* Se o tamanho da senha é menor que 6 ou maior que 32;
* Se o caractere é de pontuação, acentuação ou espaço(caracteres especiais);

Quando qualquer uma dos pontos acima é verdadeiro, a senha não é válida, assim a variável `ehInvalida` recebe 1 e usamos um `break` para parar a execução do loop.

```c
for (i = 0; i < tam; i++)
{
    if (senha[i] == 32)
    {
        ehInvalida = 1;
        break;
    }
    else if (strlen(senha) < 6 || strlen(senha) > 32)
    {
        ehInvalida = 1;
        break;
    }
    else if ((senha[i] < 48) || (senha[i] > 57 && senha[i] < 65) || senha[i] > 122 ) //pontuação e caracteres especiais
    {
        ehInvalida = 1;
        break;
    }
    else if (senha[i] >= 91 && senha[i] < 97) //pontuação e caracteres especiais
    {
        ehInvalida = 1;
        break;
    }
}
```

Esse conjunto de condicionais verifica, respectivamente se o caractere atual é um número, uma letra maiúscula ou uma letra minúscula. Se em qualquer caso for verdadeiro as váriáveis `numero`, `maiuscula` e `minuscula` recebe 1, indicando que existe pelo menos um número, letra maiúscula ou minúscula na `senha`.

```c
if (senha[i] > 47 && senha[i] < 58) //numero
    numero = 1;
else if (senha[i] > 64 && senha[i] < 91) // maiusculo
    maiuscula = 1;
else if (senha[i] > 96 && senha[i] < 123) // minuscula
    minuscula = 1;
```

Ao sair do loop, verificamos se a venha é válida ou não, e imprimimos a resposta.

```c
if (ehInvalida == 1)
    printf("Senha invalida.\n");
else if (numero == 0 || (maiuscula == 0 || minuscula == 0))
    printf("Senha invalida.\n");
else
    printf("Senha valida.\n");
```
 
Caso tenha alguma dúvida sobre este problema ou sobre a resolução, entre em contato com o PET-BCC pelo nosso
[Facebook](https://www.facebook.com/petbcc/),
[Instagram](https://www.instagram.com/petbcc.ufscar/)
ou nos mande um e-mail com o assunto "URI" para  petbcc.ufscar@gmail.com