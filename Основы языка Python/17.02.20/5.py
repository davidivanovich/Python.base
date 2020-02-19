revenue = int(input('Введите выручку - '))
costs = int(input('Введите издержки - '))
profit = (revenue - costs) / revenue
if revenue > costs:
    print('Ура! Прибыль! рентабильность выручки составила {}'.format(profit))
elif revenue == costs:
    print('В этом периоде вы работали в 0.')
else:
    print('Убытки')
