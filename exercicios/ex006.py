# Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês.

# Solicita ao usuário que informe o valor ganho por hora
valor_por_hora = float(input("Informe quanto você ganha por hora: "))

# Solicita ao usuário que informe o número de horas trabalhadas no mês
horas_trabalhadas = float(input("Informe o número de horas trabalhadas no mês: "))

# Calcula o salário total (Salário = valor por hora * horas trabalhadas)
salario = valor_por_hora * horas_trabalhadas

# Exibe o salário total
print(f"O seu salário no mês será de R$ {salario:.2f}.")

'''
Entrada de dados:

O programa pede ao usuário que informe quanto ganha por hora e o número de horas trabalhadas no mês. Ambos os valores são convertidos para float para permitir valores com casas decimais.
Cálculo do salário:

O salário é calculado multiplicando o valor por hora pelo número de horas trabalhadas.
Exibição do resultado:

O resultado final é exibido com a função print(), formatado para duas casas decimais (:.2f).
'''
