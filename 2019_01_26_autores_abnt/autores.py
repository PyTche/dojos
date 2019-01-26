def formata_nome(nome):
    SUFIXO_NOMES = [
      'FILHO',
      'FILHA',
      'NETO',
      'NETA',
      'SOBRINHO',
      'SOBRINHA',
      'JUNIOR'
    ]
    PREPOSICAO = [
        'de',
        'do',
        'da',
        'dos',
        'das'
    ]
    lnome = nome.split()
    if len(lnome) == 1:
       return lnome[0].upper()

    primeiro_nome = lnome[0]
    if lnome[-1].upper() in SUFIXO_NOMES and len(lnome)>2:
        ultimo_nome = ' '.join(lnome[-2:]).upper()
        no_meio =  [x[0].upper() if x not in PREPOSICAO else x for x in lnome[1:-2]]
    else:    
        ultimo_nome = lnome[-1].upper()
        no_meio =  [x[0].upper() if x not in PREPOSICAO else x for x in lnome[1:-1]]
    
    return ' '.join(
        [
            ultimo_nome + ',', 
            primeiro_nome, 
            ' '.join(no_meio)
        ]).strip()

