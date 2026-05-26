# Projeto v. 0.0.1

## Projeto de interface com o usuário
<!-- A partir dos requisitos criar uma interface com o usuário seja ela de texto (linha de comando), seja ela ou gráfica. -->

A interface será de linha de comando.

## Tipo de aplicação e arquitetura 
<!-- Diz respeito a decisões referentes à organização do código em funçõões, métodos, classes, módulos, subpacotes e pacotes. O problema que é dado que determina como é a melhor forma de resolver. Um programa científico por exemplo é melhor resolvido com arquitetura de programação funcional (sem procedimentos) em pipes and filters (arq). O tipo de aplicação define o tipo de arquitetura, e essa por sua vez define o paradigma de programação mais adequado a ser usado. Aqui também pode ser definida a melhor linguagem para o projeto -->

A aplicação será desenvolvida em python.

A aplicação conterá dois módulos, ambos dentro de um único pacote. Os nomes dos módulos serão os seguintes:
1. __main__
2. LivroTexto

## Projeto de dados e algoritmos
<!-- Os dados deverão ser alocados em estruturas de dados nativas ou classes criadas pelo programador. Os algoritmos estarão implementados nas funções ou métodos a depender do paradigma de programação utilizado. Quando for necessário ter banco de dados, aqui também se planeja a implementação dele. Mas não se faz o início do desenvolvimento do algoritmo aqui ainda. -->

A classe LivroTexto deverá conter os seguintes atributos e tipos:
1. titulo: str
2. autor: str
3. preco: float

Haverá um método com a seguinte assinatura:

desconto(preco: float) -> float