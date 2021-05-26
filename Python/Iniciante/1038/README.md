# [Problema URI 1038](https://www.urionlinejudge.com.br/judge/pt/problems/view/1038)

Com base na tabela abaixo, escreva um programa que leia o código de um item e a quantidade deste item. A seguir, calcule e mostre o valor da conta a pagar.

| CÓDIGO  | ESPECIFICAÇÃO |  PREÇO |
|---------|---------------|--------|
|    1    |Cachorro Quente| R$ 4.00|
|    2    |X-Salada       | R$ 4.50|
|    3    |X-Bacon        | R$ 5.00|
|    4    |Torrada Simples| R$ 2.00|
|    5    |Refrigerante   | R$ 1.50|

Problema completo: [https://www.urionlinejudge.com.br/judge/pt/problems/view/1038](https://www.urionlinejudge.com.br/judge/pt/problems/view/1038)

# Resolução

Como descrito na introdução, obteremos do usuário uma mesma linha com dois dados, sendo um o item a ser pedido e o outro a quantidade pedida, eles serão separados por um espaço vazio. Então para a obtenção dos dados usaremos a função `input()` com um parâmetro de `split(" ")` para separarmos os dados, após a obtenção de dados, será gerado um vetor com os dados e para melhor visualização separamos na variável `item` e a variável `qtd_item`, sendo ambos um número inteiro.

```python
    #Declaração de variáveis, para item e a quantidade do item que será comprado.
    entrada = input().split(' ') #Será feita uma lista com 2 espaços, sendo o primeiro qual tipo de item, e o segundo a quantidade deste.

    #Distribuindo os valores de entrada em variáveis para melhor exemplificação.
    item = int(entrada[0])
    qtd_item = int(entrada[1])
```

Após a obtenção é necessário fazer saber qual é o item pedido, pois cada item tem seu preço, e calcular o valor total a ser pago pelo cliente, deste modo é usado as funções condicionais `if` e `elif`, que é a junção de `else`+`if`. E aproveitar para calcular o `preco_total` certo para cada pedido.

``` python
    if(item==1):
        preco_total = 4.00*qtd_item
    elif(item==2):
        preco_total = 4.50*qtd_item
    elif(item==3):
        preco_total = 5.00*qtd_item
    elif(item==4):
        preco_total = 2.00*qtd_item
    elif(item==5):
        preco_total = 1.50*qtd_item
```

Para finalizar apenas apresente a saída desejada com duas casas decimais da seguinte forma: `"Total: R$ %.2f"`.

```python

    entrada = input().split(' ') #Será feita uma lista com 2 espaços, sendo o primeiro qual tipo de item, e o segundo a quantidade deste.

    item = int(entrada[0])
    qtd_item = int(entrada[1])

    if(item==1):
        preco_total = 4.00*qtd_item
    elif(item==2):
        preco_total = 4.50*qtd_item
    elif(item==3):
        preco_total = 5.00*qtd_item
    elif(item==4):
        preco_total = 2.00*qtd_item
    elif(item==5):
        preco_total = 1.50*qtd_item

    print("Total: R$ %.2f" %preco_total)
```