while True:
    try:
        # Solicita a quantidade de RA's que o programa deve considerar
        quantidade = int(input(''))

        # Loop para processar cada RA
        for i in range(quantidade):
            # Lê um RA da entrada
            RA = input('')

            # Verifica se o RA atende aos critérios (inicia com 'RA' e possui 20 caracteres)
            if RA.startswith('RA') and len(RA) == 20:
                # Obtém a senha provisória removendo 'RA' e zeros à esquerda
                senha_provisoria = RA[2:].lstrip('0')

                # Verifica se a senha provisória não é uma string vazia
                if senha_provisoria:
                    # Se não for vazia, imprime a senha provisória
                    print(senha_provisoria)
                else:
                    # Se for vazia, indica "INVALID DATA"
                    print('INVALID DATA')
            else:
                # Se o RA não atender aos critérios, indica "INVALID DATA"
                print('INVALID DATA')

    except EOFError:
        # Se ocorrer EOFError, encerra o loop
        break
