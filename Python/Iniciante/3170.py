# Problema 3170 - Beecrowd - Iniciante - Nível 1

# Ler quantidade bolinhas e de galhos
bolinhas_quantidade = int(input())
galhos_quantidade = int(input())

# Arredondando par baixo
if(galhos_quantidade % 2 != 0):
  galhos_quantidade = galhos_quantidade - 1

# Conferindo se as bolinha são suficiente e imprimindo a resposta 
if(galhos_quantidade <= bolinhas_quantidade * 2):
  print("Amelia tem todas bolinhas!")
else:
  # Cálculo de bolinhas que faltam
  resto = (galhos_quantidade - (2*bolinhas_quantidade)) / 2
  print(f'Faltam {resto:.0f} bolinha(s)')
  