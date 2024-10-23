min = int(input("ВВедите количество минут: "))
hour = min // 60
print (f'Количество часов в {min} минутах = {hour}') 
result_min = min % 60
print (f'Остаётся минут {result_min}')