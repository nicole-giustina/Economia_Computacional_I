# Documento de Requisitos
## Programa: oferta_demanda
## Descrição: este programa lê do teclado os coeficientes angular e linear das funções de oferta e damanda linear e calcula o preço de equilíbrio.
## Autor: Nicole Giustina
## Data: 30.06.2026
## Versão 0.0.1

A aplicação deve:

- Ler quatro coeficientes do teclado (a, b, c, d)
- Certificar que apenas números foram digitados pelo usuário
- Certificar que a e c são maiores que 0
- Certificar que b é negativo
- Certificar que d é positivo ou igual a 0
- Caso haja algum erro, a aplicação deve informar e solicitar a correção ao usuário (e permitir a correção)
- Confirmar os coeficientes antes de calcular
- Calcular equilibrio (a-c)/(d+b)
- Em qualquer caso, se o equilíbrio se der com preço ou quantidade negativa a aplicação deve informar ao usuário que o mercado se apresenta em desequilíbrio
- A saída de dados deve ser apresentada na tela do terminal