# 1.2.2
## Este programa imprime na tela a informação se um número digitado pelo usuário é par ou impar

#Memória e Entrada
numero = 0.0
numero = float(input('\nDigite um número: '))

#Processamento e saída
if numero < 0:
    print('Este número é inválido.')
elif numero % 1 != 0:
    print('Este número é decimal.')
elif numero % 2 == 0:
    print('Este número é par.')
else:
    print('Este número é impar.')