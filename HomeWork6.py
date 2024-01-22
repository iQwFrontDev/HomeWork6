# Задание №1 Печатные газеты использовали свой формат дат для каждого выпуска.  Для каждой газеты из списка напишите
# формат указанной даты для перевода в объект datetime:
from datetime import datetime as dt
from datetime import timedelta
the_moscow_times = 'Wednesday, October 2, 2002'
the_guardian = 'Friday, 11.10.13'
daily_news = 'Thursday, 18 August 1977'

the_moscow_times_datetime = dt.strptime(the_moscow_times, '%A, %B %d, %Y')
the_guardian_datetime = dt.strptime(the_guardian,'%A, %d.%m.%y')
daily_news_datetime = dt.strptime(daily_news,'%A, %d %B %Y')
print(the_moscow_times_datetime)
print(the_guardian_datetime)
print(daily_news_datetime)

#Задание №2 Дан поток дат в формате YYYY-MM-DD, в которых встречаются некорректные значения: Напишите функцию,
# которая проверяет эти даты на корректность.  То есть для каждой даты возвращает True — дата корректна или False — некорректная.

stream = ['2018-04-02', '2018-02-29', '2018-19-12']
def correct_date(date):

    for date_ in date:
        try:
            datetime_ = dt.strptime(date_,'%Y-%m-%d')
            print(True)
        except ValueError:
            print(False)


correct_date(stream)

#Задание №3 Напишите функцию date_range, которая возвращает список дат за период от start_date до end_date. Даты
# должны вводиться в формате YYYY-MM-DD.  В случае неверного формата или при start_date > end_date должен возвращаться пустой список.

def date_range(start_date, end_date):
    format = "%Y-%M-%d"

    try:
        s_date = dt.strptime(start_date,format)
        e_date = dt.strptime(end_date,format)
        diff = e_date - s_date
        lst_date = [dt.strftime(s_date + timedelta(days=x), format) for x in range(diff.days + 1)]
        return print(lst_date)
    except (ValueError, s_date > e_date):
        lst_date = []
        return print(lst_date)

date_range(start_date='2024-01-21', end_date='2024-01-30')
