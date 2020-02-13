hour, minute, second = int(input('Введіть години: ')), \
                       int(input('Введіть хвилини: ')), \
                       int(input('Введіть секунди: '))
if(0 <= hour <= 11)and(0 <= minute <= 59)and(0 <= second <= 59):
    all_second = hour * 3600 + minute * 60 + second
    corner = all_second * 0.0083
    print(f'За {hour} годин {minute} хвилин {second} секунд стрілка пройде на {corner} градусів')
else:
    print('Дані введено не коректно')
