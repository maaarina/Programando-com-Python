#Faça um Programa que peça as 4 notas bimestrais e mostre a média.

nota1 = float(input("Informe a primeira nota: "))
nota2 = float(input("Informe a segunda nota: "))
nota3 = float(input("Informe a terceira nota: "))
nota4 = float(input("Informe a quarta nota: "))

# Calcula a média das quatro notas
media = (nota1 + nota2 + nota3 + nota4) / 4

# Exibe a média das notas
print(f"A média das notas é {media:.2f}.")

'''
Entrada de dados:

O programa utiliza a função input() quatro vezes para pedir as notas bimestrais, convertendo-as para o tipo float com a função float().
Cálculo da média:

A soma das quatro notas é dividida por 4 para calcular a média.
Exibição do resultado:

A função print() exibe a média calculada. Usamos :.2f para limitar o resultado a duas casas decimais.
'''