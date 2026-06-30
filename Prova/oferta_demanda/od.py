def equilibrio(coeficientes_demanda, coeficientes_oferta):
    """calcula preço de equilíbrio"""
    preco = 0.0
    preco = (coeficientes_demanda[0] - coeficientes_oferta[0]) / (coeficientes_oferta[1] + coeficientes_demanda[1])
    if preco < 0:
        print('O mercado está em desequilibrio nestas condições')
    else:
        return preco