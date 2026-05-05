def leitura_dados():
    """Entrada de dados"""
    dados = [0,0]
    i=0
    while i<2:
        dados[i]=float(input(f'\nDigite a parcela {i+1}: '))
        i+=1
    return dados

def saida(lista, resultado):
    """Saída de dados"""
    print(f'\nA soma da parcela {lista[0]} com a parcela {lista[1]} é igual a {resultado}\n')