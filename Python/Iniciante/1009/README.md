```# [Problema URI 1009:](https://www.urionlinejudge.com.br/judge/pt/problems/view/1009)

---

Faça um programa que leia o nome de um vendedor, o seu salário fixo e o total de vendas efetuadas por ele no mês (em dinheiro). Sabendo que este vendedor ganha 15% de comissão sobre suas vendas efetuadas, informar o total a receber no final do mês, com duas casas decimais.

**Problema completo:** [https://www.urionlinejudge.com.br/judge/pt/problems/view/1009](https://www.urionlinejudge.com.br/judge/pt/problems/view/1009)

# Resolução:

---

Como descrito na introdução, o desafio é bastante simples, será necessário ler um nome, salário fixo e o valor total de vendas de um funcionário, e dar como saída o valor total recebido pelo o funcionário.

Para a obtenção dos dados é usado a função input da linguagem, porém como esta função retorna um dado do tipo *`string`,* para valores como o salário e o total de vendas do funcionário é necessário usar um *`cast`*, que força um dado ser do tipo do *`caster`*. Como nas linhas a seguir:

```python
#Declaração e obtenção de dados do usuário
nome = input()
salario = float(input()) #Uso do caster float()
total_vendas = float(input()) #Uso do caster float()
```

E para o calculo do valor total que o funcionário deva receber foi inicializado uma variável chamada *`total_recebido`,* que já receberá o valor do salário mais 15% do total de vendas que ele fez no mês. E para apresentar este valor ao usuário usa-se a função *`print`* com o parâmetro *`%.2f`*, para limitar a apenas duas casas decimais do número real.

```python
total_recebido = salario + (total_vendas*0.15)
print("TOTAL = R$ %.2f" %total_recebido)
```

O código completo é dado como:

```python
nome = input()
salario = float(input())
total_vendas = float(input())

total_recebido = salario + (total_vendas*0.15)
print("TOTAL = R$ %.2f" %total_recebido)
```