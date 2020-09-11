# Problema:

Larissa é uma acadêmica muito inteligente e estudiosa, com isso ela é engajada em várias atividades. Chegou o final do ano, mês da sua apresentação de TCC. Ela, muito atarefada, precisa saber se vai conseguir realizar sua apresentação antes do Natal! Mas antes de sua apresentação ela deve passar por uma verificação com sua orientadora oriental, a Prof.Takanada (/Tá com nada/).

**Problema Completo:** https://www.urionlinejudge.com.br/judge/pt/problems/view/2930

# Resolução:

Para resolver este problema, primeiramente devemos declarar as variáveis que serão utilizadas no exercício em questão, que no caso são as seguintes variáveis do tipo inteiro: `dia_que_foi_entregue` e `data_final_pra_entregar`.

```c
int dia_que_foi_entregue, data_final_pra_entregar;
```

Após informarmos as variáveis que serão utilizadas no decorrer do problema, usamos o comando `scanf` para lermos os valores de `dia_que_foi_entregue` e `data_final_pra_entregar`.

```c
scanf("%d %d",&dia_que_foi_entregue,&data_final_pra_entregar);
```

Em seguida, é feito uma estrutura de seleção `if` para que cada um dos casos descritos no problema seja seja avaliado e em sequida seja escrita a frase em questão.

O primeiro `if` é para o caso que verifica se a acadêmica apresentará ou não. A única possibilidade da entrega não ser realizada na data é por falta de orientação da Takanada. E caso não seja possivel, é escrito através do comando `printf` a frase "Eu odeio a professora!".

Em seguida, o primeiro `else if` é para o caso em que a apresentação é entregue em até 3 dias antes do prazo final, e neste caso, através do comando `printf`, é escrito "Muito bem! Apresenta antes do Natal!"

Na sequencia, o segundo `else if` é para o caso contrário, no qual a data de apresentação é muito próximo da data limite, (no caso é menos de dois dias), e aí é escrito através do comando `printf` a frase "Parece o trabalho do meu filho!"

```c
if (dia_que_foi_entregue > data_final_pra_entregar)
{
printf("Eu odeio a professora!\n");
}
else if (dia_que_foi_entregue+2 <= data_final_pra_entregar)
{
printf("Muito bem! Apresenta antes do Natal!\n");
}
else if ( data_final_pra_entregar-dia_que_foi_entregue < 2 )
{
printf("Parece o trabalho do meu filho!\n");
        
    /**
     * Nova estrutura if-else aqui.
    **/

}
```

Dentro do segundo `else if` é adicionado nova estrutura de desicão, que conta com um `if` e um `else`. E esta estrutura faz a seguinte analise: É adicionado mais dois dias (a `data_final_pra_entregar` é aumentada em 2), e com o `if` verificamos se essa nova data final é menor que a véspera do natal (24), e caso seja, ela poderá apresentar o trabalho final, e é impresso através do comando `printf` a frase "TCC Apresentado!", e a estrutura `else` é para o caso contrário e com o comando `printf` é impresso "Fail! Entao eh nataaaaal!"

```c
if ( data_final_pra_entregar+2 <= 24)
    {
    printf("TCC Apresentado!\n");
    }
    else
    {
    printf("Fail! Entao eh nataaaaal!\n");
    }
```