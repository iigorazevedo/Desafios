speed = int(input('Qual a velocidade do veículo?'))
print('A velocidade acima de 80km/h gera uma multa')
if speed >= 80:
    print(f'Você foi multado em R$ {(speed-80)*7:.2f}')
else:
    print('Parabéns, você estava dentro do limite de velocidade!')
print('--FIM--')