"""
Programa: Adulto_menor
Descrição: este programa pergunta a idade de uma pessoa e, dependendo da idade, apresenta a mensagem 'Oi! Você é um adulto.' ou 'Oi! Você é menor de idade'.
Nome: Nicole Schultz
Data: 24/03/2026
Versão 0.0.1
"""

# Alocação de memória
idade = 0
texto = ""

# Entrada de dados
idade = int(input("\nQual a sua idade? "))

# Processamento
if idade >= 18:
    texto = 'Oi! Você é um adulto.'
else:
    texto = 'Oi! Você é menor de idade.'

# Saída
print(texto)
