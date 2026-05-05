# Definição de funções

def leitura_dados():
    """Entrada de dados"""
    dados = [0,0]
    i=0
    while i<2:
        dados[i]=float(input(f'\nDigite a parcela {i+1}: '))
        i+=1
    return dados

def soma (x,y):
    """Processamento de dados"""
    return x+y

def saida(lista, resultado):
    """Saída de dados"""
    print(f'\nA soma da parcela {lista[0]} com a parcela {lista[1]} é igual a {resultado}\n')

def main():
    # Entrada de dados
    dados = leitura_dados()

    # Processamento
    resultado = soma(dados[0], dados[1])

    # Saída
    saida(dados, resultado)

if __name__ == '__main__':
    main()
    
    