import re

def validar_senha(senha):
    # Verificar se a senha tem de 6 a 32 caracteres
    if 6 <= len(senha) <= 32:
        # Verificar se a senha contém pelo menos uma letra maiúscula, uma letra minúscula e um número
        if re.search(r'[A-Z]', senha) and re.search(r'[a-z]', senha) and re.search(r'\d', senha):
            # Verificar se a senha não contém caracteres de pontuação, acentuação ou espaço
            if re.match(r'^[a-zA-Z0-9]*$', senha):
                return "Senha valida."
            else:
                return "Senha invalida."
        else:
            return "Senha invalida."
    else:
        return "Senha invalida."

# Processar entradas até o final do arquivo
while True:
    try:
        senha = input()
        resultado = validar_senha(senha)
        print(resultado)
    except EOFError:
        break