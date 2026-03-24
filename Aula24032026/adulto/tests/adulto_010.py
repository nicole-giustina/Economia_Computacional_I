"""
Programa adulto
Descrição: este programa pergunta a idade de uma pessoa. Se a idade for maior do que 18 anos, o programa imprime na tela um texto. Esta versão corrige uma questão estética, adicionando espaço para resposta na pergunta feita.
Data: 24/03/2026
Versão 0.1.0
"""
# Alocação de memória
idade = 0
texto = ""

# Entrada
idade = int(input("\nQual a sua idade? "))

# Processamento
if idade >= 18:
    texto = 'Oi! Você é um adulto.'

# Saída
print(texto)