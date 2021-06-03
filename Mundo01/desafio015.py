km = float (input ('Insira a quantidade de quilômetros percorridos: '))
dias = int (input ('Insira a quantidade de dias que o carro foi alugado: '))
valor_km = km*0.15
valor_dias = dias*60
total = valor_km+valor_dias
print('O valor total a pagar pelo aluguel do carro é de: R$ {}'.format(total))