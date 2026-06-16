""" Este módulo é a camada de acesso a dados da aplicação. """

def reader():
     """ Esta função solicita ao usuário apra que digite até duas parcelas"""
    i = 0
    dados = [0,0]
    while i < 2:
        dados[i] = float(input(f'Digite a parcela {i+1}'))
        i+=1
    return dados
    
def writer(dados: list) -> None:
    """ Esta função escreve dados em um arquivo txt criado para isso"""
    with open('arquivo.txt', 'w') as arquivo:
        conteudo = arquivo.write(str(dados))