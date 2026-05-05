import es
# posso escrever também "from es import leitura_dados", para importar uma função única e não o módulo inteiro, caso seja melhor para otimizar e não precise todas as funções de lá. Exemplo abaixo

from aritmetico import soma

def main():
    # Entrada de dados
    dados = es.leitura_dados()

    # Processamento
    resultado = soma(dados[0], dados[1])
# Como a função soma foi importada direto, especificicada, não precisa dizer de onde foi tirada.
    
    # Saída
    es.saida(dados, resultado)

if __name__ == '__main__':
    main()