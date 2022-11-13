m = int(input('Введите номер месяца:'))
d = int(input('Введите номер дня:'))
days = 0

if m not in range(1, 13) or d not in range(1, 32):
    print('Не верно введен номер месяца или дня!')
else:
    if m < 12:
        for i in range(m, 13):
            if i in [4, 6, 9, 11]:
                days += 30
            elif i == 2:
                days += 28
            else:
                days += 31
        days -= d
    elif m == 12:
        days = 31 - d

stay = 'осталось'
text_d = ''
ldays = int(str(days)[-1:])

if 10 <= days <= 20:
    text_d = 'дней'
elif 2 <= ldays <= 4:
    text_d = 'дня'
elif ldays == 1:
    stay = 'остался'
    text_d = 'день'
else:
    text_d = 'дней'

print(f'До Нового года {stay} {days} {text_d}!')

