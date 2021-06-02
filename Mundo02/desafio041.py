from datetime import date
todays_date=date.today()
ano = int(input('Insira o ano do nascimento do atleta: '))
year = todays_date.year
soma = year - ano
if soma <= 9:
    print('Sua categoria é a mirim.')
elif soma <=14:
    print('Sua categoria é INFANTIL')
elif soma <19:
    print('Sua categoria é a JUNIOR')
elif soma <=20:
    print('Sua categoria é a SÊNIOR')
else:
    print('Sua categoria é MASTER!')
