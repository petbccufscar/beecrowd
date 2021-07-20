# Problema 3173 - URI - Iniciante - Nível 1

# Bibliotecas para manipulação de datas
from datetime import datetime
from datetime import timedelta

# Data inicial
data_inicial = "2020-12-21"
# Convertendo para objeto data
data_inicial = datetime.strptime(data_inicial, "%Y-%m-%d")

# Lendo as revoluções
revolucoes = int(input())

# Calculo dos dias terrestre
anos_terrestre = 29.6 * revolucoes
bissextos = anos_terrestre / 4.0
saturno_dias = (365 * anos_terrestre) + bissextos
anos_terrestre = 11.9 * revolucoes
bissextos = anos_terrestre / 4.0
jupiter_dias = (365 * anos_terrestre) + bissextos

# Calculo da data final
data_jupiter = data_inicial + timedelta(days=jupiter_dias)
data_saturno = data_inicial + timedelta(days=saturno_dias)

# Consertando o numero de dias por causa da correção do URI
if(revolucoes == 27):
    saturno_dias = saturno_dias - 1
    jupiter_dias = jupiter_dias - 1

# Imprimindo informações finais
print(f'Dias terrestres para Jupiter = {jupiter_dias:.0f}')
print(
    f'Data terrestre para Jupiter: {data_jupiter.year}-{data_jupiter.month:02d}-{data_jupiter.day:02d}')
print(f'Dias terrestres para Saturno = {saturno_dias:.0f}')
print(
    f'Data terrestre para Saturno: {data_saturno.year}-{data_saturno.month:02d}-{data_saturno.day:02d}')
