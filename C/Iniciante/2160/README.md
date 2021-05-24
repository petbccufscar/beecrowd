# Problema:
Preencher formulários é uma tarefa simples. Mas é preciso conferir se o espaço reservado para os dados é suficiente.

Sua tarefa é, dada uma linha de texto, indicar se ele cabe ou não cabe em um formulário com 80 caracteres.
 
 
##### Link do problema: https://www.urionlinejudge.com.br/judge/pt/problems/view/2160
 
 
# Resolução:
 
Para sabermos se a entrada digitada é menor ou igual a 80 caracteres, iremos importar a biblioteca `string.h`, para utilizarmos a função strlen() e declarar um vetor de 500 caracteres, `entrada`.

```c
char entrada[500];
```

Em seguida, lemos a entrada fornecida **até que uma quebra de linha seja lida**, não incluindo-a. Note que, caso a entrada fosse maior que a variável em que está sendo armazenada, neste caso, 500 caracteres, a função irá exibir comportamento indefinido.

```c
scanf("%[^\n]", entrada);
```

Em seguida, utilizamos a função `strlen()`, que retorna o tamanho, em caracteres, de uma string dada, para verificar se o tamanho é maior que 80:
- Se sim, exibimos `NO`;
- Se não, exibimos `YES`.

```c
if(strlen(entrada) > 80)
    printf("NO\n");
else
    printf("YES\n");
```

##### Mais a utilização do scanf: [utilização scanf para strings](https://wiki.portugal-a-programar.pt/dev_geral:c:scanfparastrings)
 
Caso tenha alguma dúvida sobre este problema ou sobre a resolução, entre em contato com o PET-BCC pelo nosso
[Facebook](https://www.facebook.com/petbcc/),
[Instagram](https://www.instagram.com/petbcc.ufscar/)
ou nos mande um e-mail com o assunto "URI" para  petbcc.ufscar@gmail.com
