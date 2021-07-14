# Problema 2754 - URI - Iniciante - Nível 1

# Atribuindo os valores necessários para a resolução do problema
num1 = 234.345
num2 = 45.698

# Apresentação da resposta desejada com os prints

# Apresentando com 6 casas decimais, a tag "f"
print(f"{num1:.6f} - {num2:.6f}")

# Apresentando como inteiros com a tag "d"
print(f"{num1:.0f} - {num2:.0f}")

# Apresentando com 1 casa decimal.
print(f"{num1:.1f} - {num2:.1f}")

# Apresentando com 2 casas decimais.
print(f"{num1:.2f} - {num2:.2f}")

# Apresentando com 3 casas decimais.
print(f"{num1:.3f} - {num2:.3f}")

# Transformando os valores em notação científica, dividindo por 10 até o valor ser menor que 10. E armazenando quantas vezes foi necessário para chegar a um valor menor que 10, em um vetor, sendo a primeira posição o valor inteiro e a segunda posição o valor da base 10 do número.
ntcNum1 = [num1, 0]
ntcNum2 = [num2, 0]
while(ntcNum1[0]>10):
  ntcNum1[0] = ntcNum1[0]/10
  ntcNum1[1] += 1
while(ntcNum2[0]>10):
  ntcNum2[0] = ntcNum2[0]/10
  ntcNum2[1] += 1

# Apresentando com notação científica com "e"
print(f"{ntcNum1[0]:.6f}e+{ntcNum1[1]:02d} - {ntcNum2[0]:.6f}e+{ntcNum2[1]:02d}")

# Apresentando com notação científica com "E"
print(f"{ntcNum1[0]:.6f}E+{ntcNum1[1]:02d} - {ntcNum2[0]:.6f}E+{ntcNum2[1]:02d}")

# Comparando o tamanho notação científica e o valor. 
# Armazenando a menor representação nas variávies "mnrStrNum1 e mnrStrNum2" 
if(len(str(num1))<len(f"{ntcNum1[0]:.6f}E+{ntcNum1[1]:02d}")):
  mnrStrNum1 = str(num1)
else:
  mnrStrNum1 = str(f"{ntcNum1[0]:.6f}E+{ntcNum1[1]:02d}")
if(len(str(num2))<len(f"{ntcNum2[0]:.6f}E+{ntcNum2[1]:02d}")):
  mnrStrNum2 = str(num2)
else:
  mnrStrNum2 = str(f"{ntcNum2[0]:.6f}E+{ntcNum2[1]:02d}")

# Apresentando a representação mais curta. 
print(f"{mnrStrNum1} - {mnrStrNum2}")

# Apresentando a representação mais curta. 
print(f"{mnrStrNum1} - {mnrStrNum2}")
