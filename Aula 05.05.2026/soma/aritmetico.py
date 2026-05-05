def soma (x,y):
    """Processamento de dados; esta função soma dois números"""
    return x+y

# posso colocar o tipo da variável e do resultado da função dessa forma com ':', sem prejuízo no funcionamento
def mult(x:float, y:float) ->float: 
    """Esta função multiplica dois números"""
    return x*y

def div(x:float, y:float) ->float:
    """Esta função divide dois números"""
    if y==0:
        resultado = 'Não é possível dividir por zero'
        return resultado
    else:
        return x/y


    
    
