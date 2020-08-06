# Problema 1564:

O Brasil é o país sede da copa esse ano. Porém, há muitas pessoas protestando contra o governo. Em redes sociais é possível ver pessoas afirmando que não vai ter copa devido aos protestos.

Mas esses rumores de que não haverá copa são totalmente falsos, a presidente Dilma Roussef já avisou: vai ter copa sim, e se reclamar vai ter duas!

###### Problema completo: https://www.urionlinejudge.com.br/judge/pt/problems/view/1564

# Resolução

O seu enunciado não é muito claro do que realmente tem que se fazer, porém a ideia é simples. O exercício irá receber uma entrada `N` que varia de 0 à 100 e caso ela for diferente de 0 a saída será **vai ter duas!** e caso for igual a 0 será **vai ter copa!**. 
O exercício ainda adiciona um caso de leitura até o final do arquivo, no qual chamamos de [EOF - End of File](https://pt.wikipedia.org/wiki/EOF), ao nível desse exercício não é nescessário dominar sua real utilização que remete à Arquivos, tópico que será trabalhado mais a frente, única coisa é ter em mente o que fazer quando o Uri pede esse tipo de leitura.

Iniciamos declarando as variáveis que serão utilizadas:

```c
        int N;
```
`N` o número que representa as "reclamações".

Fazemos a leitura do `N` no `scanf` e essa leitura é feita dentro do `while`:

```c
       while((scanf("%d", &N)!=EOF)&&(N<=100)&&(N>=0)){}
```
Dentro do `while` fazemos a leitura e comparamos ao `EOF`, portando o `while` irá rodar até chegar no "final do arquivo" que no caso será uma quebra de linha(representada por CTRL-D(linux) ou CTRL-Z (Windows)). O `while` será finalizado também caso o valor lido for maior que 100 ou menor que 0.

E o conteúdo do `while` é onde mora a resposta do exercício:
```c
        while ((scanf("%d", &N)!=EOF)&&(N<=100)&&(N>=0))
        {
                if(N==0){
                        printf("vai ter copa!\n");
                }
                else{
                        printf("vai ter duas!\n");
                }
        }
```
No `if` é verificado se `N` é igual 0 o que resulta na saída "vai ter copa" ou se ele é outro valor, dentro do intervalo explicado anteriormente, no qual resulta a saída "vai ter duas"

Caso tenha alguma dúvida sobre este problema ou sobre a resolução, entre em contato com o PET-BCC pelo nosso
[Facebook](https://www.facebook.com/petbcc/),
[Instagram](https://www.instagram.com/petbcc.ufscar/)
ou nos mande um e-mail com o assunto "URI" para petbcc.ufscar@gmail.com


