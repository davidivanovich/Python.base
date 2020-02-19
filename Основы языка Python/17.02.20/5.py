revenue = int(input('Введите выручку - '))
costs = int(input('Введите издержки - '))
profit = (revenue - costs) / revenue
if revenue > costs:
    print('Ура! Прибыль! рентабильность выручки составила {}'.format(profit))
    workers = int(input('Введите колличество сотрудников.'))
    p_w = (revenue - costs) / workers
    print('Прибыль в пересчете на работников равна {} на человека'.format(p_w))
elif revenue == costs:
    print('В этом периоде вы работали в 0.')
else:
    print('Убытки')
