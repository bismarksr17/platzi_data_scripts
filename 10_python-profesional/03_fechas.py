import datetime

'retorna la fecha actual'
'si se trabaja en la una computadora local, retorna la fecha del sistema'
'si se trabaja en un servidor, retorna en forma UTC'
my_time = datetime.datetime.now()
print(my_time)

'retorna la fecha actual'
muy_day = datetime.datetime.today()

'extraer año, mes y dia'
print(f'Year: {muy_day.year}')
print(f'Month: {muy_day.month}')
print(f'Day: {muy_day.day}')

'tabla de codigos de formato de fechas'
'https://i.imgur.com/mY5meK8.png'

my_str = my_time.strftime('%d/%m/%Y')
print(f'Formato LATAN: {my_str}')

my_str = my_time.strftime('%m/%d/%Y')
print(f'Formato EEUU: {my_str}')

my_str = my_time.strftime('Este es el año %Y')
print(f'Formato random: {my_str}')