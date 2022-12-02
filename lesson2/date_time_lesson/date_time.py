from datetime import datetime, timedelta

one_day = 1
days_ago = 30

date_now = datetime.now()
delta = timedelta(days=one_day)
print(f'Вчера было: {date_now - delta}')
print(f'Сегодня {date_now}')
delta = timedelta(days=days_ago)
print(f'{days_ago} дней назад было {date_now - delta}')

input_datastring = '01/01/25 12:10:03.234567'
date_from_string = datetime.strptime(input_datastring, '%d/%m/%y %H:%M:%S.%f')
print(date_from_string)
