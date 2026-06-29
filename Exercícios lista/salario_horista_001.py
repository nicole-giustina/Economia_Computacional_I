"""
# Este programa calcula o salário de um trabalhador horista. Ele pergunta o número de horas trabalhadas, o valor da hora, calcula e imprimir na tela o valor do salário bruto, líquido e o total de descontos
## Versão 0.0.1
## 18/06/2026
## Nicole S. D Giustina
"""

#Memória
n_horas = 0
v_hora = 0.0
salario_bruto = 0.0
salario_liq = 0.0

#Entrada
n_horas = int(input(f'\nQuantas horas você trabalhou esse mês? '))
v_hora = float(input(f'\nQual o valor contratual da sua hora de trabalho? '))

#Processamento
salario_bruto = n_horas * v_hora
salario_liq = salario_bruto * 0.7

#Saída
print(f'\nSeu salário bruto é {salario_bruto}, mas considerando os descontos você deve receber em torno de {salario_liq}.')