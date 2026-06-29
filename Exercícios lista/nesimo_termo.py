"""
## 1.1.5
# Este programa determina o n-ésimo termo de uma PA onde n e q são dados pelo usuário.
"""
#Memória
a1 = 0.0
q = 0.0
n_esimo = 0.0
qnesimo = 0
#Entrada
a1 = float(input(f'\nDigite o termo inicial da PA: '))
q = float(input(f'\nAgora digite a razão dessa PA: '))
qnesimo = int(input('\nQual termo da PA você quer saber? '))
#processamento
n_esimo = a1 + (qnesimo - 1) * q
print(f'\nO valor do termo {qnesimo} é {n_esimo}.')