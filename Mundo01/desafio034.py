salario = float(input('Qual o salário do funcionário? '))
if salario <= 1250:
    aumento = 1.15
else:
    aumento = 1.10
n_salario = salario * aumento
print(f'O novo salário será de R${n_salario:.2F}')
