km = int(input('Digite a distância da viagem: '))
if km <= 200:
    preco = 0.50
else:
    preco = 0.45
passagem = km * preco
print(f'Você irá pagar R$ {passagem:.2f} de passagem!')