def soma (x,y):
    """Processamento de dados"""
    return x+y



def main():
    # Entrada de dados
    dados = leitura_dados()

    # Processamento
    resultado = soma(dados[0], dados[1])

    # Saída
    saida(dados, resultado)

if __name__ == '__main__':
    main()
    
    