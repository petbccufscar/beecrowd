# Problema 3161 - Beecrowd - Iniciante - Nível 1

# Ler quantidade de frutas e linhas da lista
entrada = input().split()
quantidade_frutas = int(entrada[0])
linhas_lista = int(entrada[1])

# Criar vetor vetor_frutas de tamanho quantidade_frutas
vetor_frutas = [""]*quantidade_frutas

# Criar vetor vetor_linhas de tamanho linhas_lista
vetor_linhas = [""]*linhas_lista

# Ler a fruta e coloca-la em minusculo
for i in range(quantidade_frutas):
  vetor_frutas[i] = input().lower()    

# Ler a fruta codificada e coloca-la em minusculo
for i in range(linhas_lista):
  vetor_linhas[i] = input().lower()  

# Invertendo a escrita lida para decodificar a fruta
for i in vetor_frutas:
  Come = False
  fruta_inversa = i[::-1] 
  # Verificar se come a fruta
  for j in vetor_linhas:
    if (i in j) or (fruta_inversa in j):
      Come = True
      break
  # Escrita da saída com verificação se come ou não
  if Come:
    print("Sheldon come a fruta", i)
  else:
    print("Sheldon detesta a fruta", i)