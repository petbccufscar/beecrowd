# Problema:   

Devita é o príncipe dos Calsadins. Juntamente com Pana, eles vão atrás de Tataroko, o nome de nascimento de Kogu, para tentar dominar o mundo. Ele possui um rastreador que mede o nível de energia de qualquer ser vivo. Todos os seres com o nível menor ou igual a 8000, ele considera como se fosse um inseto. Quando passa deste valor, que foi o caso de Kogu, ele se espanta e grita “Mais de 8000”. Baseado nisso, utilize a mesma tecnologia e analise o nível de energia dos seres vivos.

**Problema Completo**: https://www.urionlinejudge.com.br/judge/pt/problems/view/2862

# Resolução:

O exercício consiste em receber um valor inteiro e verificar se é maior que 8000. Em uma clara referencia a Gradon Ball X, devemos imprimir "Mais de 8000!" na tela se sim, ou "Inseto!" caso contrário.

Começamos declarando as variáveis que devemos utilizar:
- `C` para o número de casos;
- `N` para o nível de energia, e;
- `i` para contar cada caso de teste.

```c
int C, N, i;
```

Fazemos a leitura do número de casos com a função `scanf()`.

```c
scanf("%d", &C);
```

Em seguida, para cada caso de teste, fazemos a leitura do nível de poder na variável `N`.

```c
for (i = 0; i < C; i++) {
        scanf("%d", &N);
```

Se o nível for maior que 8000, imprimimos "Mais de 8000!" na tela e pulamos para a próxima linha. Note que a condição é estritamente maior que 8000, ou seja, a partir de 8001. Se não, imprimimos "Inseto!" e também pulamos a linha.

```c
    if (N > 8000) {
        printf("Mais de 8000!\n");
    } else {
        printf("Inseto!\n");
    }
}
```

##### Para revisar sobre entradas e saídas em C: [Entrada e Saida](http://linguagemc.com.br/operacoes-de-entrada-e-saida-de-dados-em-linguagem-c/)
##### Para aprender um pouco mais sobre a estrutura for: [O laço FOR](https://www.cprogressivo.net/2013/02/O-que-e-para-que-serve-e-como-usar-o-laco-FOR-em-C.html) 


Caso tenha alguma dúvida sobre este problema ou sobre a resolução, entre em contato com o PET-BCC pelo nosso
[Facebook](https://www.facebook.com/petbcc/),
[Instagram](https://www.instagram.com/petbcc.ufscar/)
ou nos mande um e-mail com o assunto "URI" para  petbcc.ufscar@gmail.com
