def entrada_coeficientes():
    """Entrada de coeficientes"""
    coeficientes_demanda = ['linear_a', 'angular_b']
    coeficientes_oferta = ['linear_c', 'angular_d']
    i=0
    while i<2:
        coeficientes_demanda[i]=float(input(f'\nDigite o coeficiente {coeficientes_demanda[i]} da demanda: '))
        if i == 0 and coeficientes_demanda[i] <= 0:
            print('\nO coeficiente linear deve ser positivo. Tente novamente')
            continue
        elif  i == 1 and coeficientes_demanda[i] > 0:
            print('\nO coeficiente angular deve ser igual ou menor que zero. Tente inserir outro número para esse coeficiente')
            continue
        else:
            i+=1
    i=0
    while i<2:
        coeficientes_oferta[i]=float(input(f'\nDigite o coeficiente {coeficientes_oferta[i]} da oferta: '))
        if coeficientes_oferta[i] <= 0:
            print('\nO coeficiente linear deve ser positivo e o angular deve ser igual ou menor que zero. Tente inserir outro número para esse coeficiente')
            continue
        else:
            i+=1
    return coeficientes_demanda, coeficientes_oferta

def saida_dados(preco):
    """Saída de dados"""
    print(f'\nO preço de equilíbrio para estes coeficientes é {preco}')