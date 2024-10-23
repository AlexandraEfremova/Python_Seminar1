number = int(input("Введите шестизначное число: "))
num1 = number // 100000
num2 = (number % 100000) // 10000
num3 = (number % 10000) // 1000
num4 = (number % 1000) // 100
num5 = (number % 100) // 10
num6 = number % 10
sum1 = num1 + num2 + num3
sum2 = num4 + num5 + num6
if sum1 == sum2:
    print("Yes")
else:
    print("No")