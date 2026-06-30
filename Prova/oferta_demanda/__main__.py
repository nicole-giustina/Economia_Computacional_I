import es as es
import od as od

def main():
    coeficientes_demanda, coeficientes_oferta = es.entrada_coeficientes()
    resultado = od.equilibrio(coeficientes_demanda, coeficientes_oferta)
    es.saida_dados(resultado)

main()