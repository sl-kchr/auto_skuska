#ex 1 Напиши функцию, которая будет принимать дату рождения в формате YYYY-MM-DD и возвращать количество дней до следующего дня рождения. Используй модуль datetime и timedelta для вычислений.
from datetime import datetime, timedelta, date, time
def next_bd (bd):
    try:
        bd = datetime.strptime(bd, '%Y-%m-%d')
    except ValueError:
        bd = datetime.strptime(bd, '%Y.%m.%d')
    if bd.year % 4 != 0:
        bd += timedelta(days=365)
    else:
        bd += timedelta(days=366)
    print(bd)
    return bd
next_bd ('2003-03-22')