# Problema 1040 - Beecrowd - Iniciante - Nível 5

# Recebe os valores para as quatro notas
nota1, nota2, nota3, nota4 = map(float, input().split())

# Calcula a média ponderada
media = (nota1*2 + nota2*3 + nota3*4 + nota4)/(2 + 3 + 4 + 1)
print(f"Media: {media:.1f}")

# Verifica se o aluno foi aprovado
if media >= 7:
    print("Aluno aprovado.")

# Verifica se o aluno está habilitado para recuperação
# caso não tenha sido aprovado de imediato
elif media >= 5:
    print("Aluno em exame.")

    # Recebe a nota do exame
    nota5 = float(input())
    print("Nota do exame: {:.1f}".format(nota5))
    media = (media + nota5)/2

    # Verifica se o aluno foi aprovado após o exame
    if media >= 5:
        print("Aluno aprovado.")
    else:
        print("Aluno reprovado.")

    # Imprime a média final
    print(f"Media final: {media:.1f}")
else:
    print("Aluno reprovado.")
