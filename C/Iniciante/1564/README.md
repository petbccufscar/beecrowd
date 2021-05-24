# Problema:

O Brasil é o país sede da copa esse ano. Porém, há muitas pessoas protestando contra o governo. Em redes sociais é possível ver pessoas afirmando que não vai ter copa devido aos protestos.

Mas esses rumores de que não haverá copa são totalmente falsos, a presidente Dilma Roussef já avisou: vai ter copa sim, e se reclamar vai ter duas!

###### Problema completo: https://www.urionlinejudge.com.br/judge/pt/problems/view/1564

# Resolução

O exercício recebe uma entrada `N` (variando de 0 à 100) e, caso esta for diferente de 0, a saída será **"vai ter duas!"**, caso for igual a 0, será **"vai ter copa!"**
O exercício aborda um caso de leitura em que deve ser lido até o final do arquivo [EOF - End of File](https://pt.wikipedia.org/wiki/EOF). Considerando o nível desse exercício, não é necessário dominar a utilização de arquivos (tópico que será trabalhado mais a frente), basta ter conhecimento da informação citada para quando deparar-se com esse tipo de leitura.

Iniciamos declarando a variável `N`, a única a ser utilizada e que representa o número de reclamações recebidas.

```c
        int N;
```
Fazemos a leitura do `N` no `scanf` e essa leitura é feita dentro do `while`:

```c
       while(scanf("%d", &N)!=EOF){}
```
Dentro do `while` fazemos a leitura e comparamos ao EOF, portanto o while irá rodar até chegar no final do arquivo. Este é simbolizado pela quebra de linha ("\n"), que pode ser representada por CTRL+D no Linux  ou CTRL+Z no Windows.

A lógica presente no interior da estrutura `while` contém a resolução do exercício:
```c
        while (scanf("%d", &N)!=EOF)
        {
                if(N==0){
                        printf("vai ter copa!\n");
                }
                else{
                        printf("vai ter duas!\n");
                }
        }
```
No `if` é verificado se `N` é igual a 0, o que resulta na saída "vai ter copa!". Caso tenha outro valor, a saída resultante será "vai ter duas!".

Caso tenha alguma dúvida sobre este problema ou sobre a resolução, entre em contato com o PET-BCC pelo nosso
[Facebook](https://www.facebook.com/petbcc/),
[Instagram](https://www.instagram.com/petbcc.ufscar/)
ou nos mande um e-mail com o assunto "URI" para petbcc.ufscar@gmail.com


