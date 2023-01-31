# Задача 6: Вы пользуетесь общественным транспортом? Вероятно, вы расплачивались за проезд
# и получали билет с номером. Счастливым билетом называют такой билет с шестизначным номером,
# где сумма первых трех цифр равна сумме последних трех. Т.е. билет с номером 385916 – счастливый,
# т.к. 3+8+5=9+1+6. Вам требуется написать программу, которая проверяет счастливость билета.
# 385916 -> yes
# 123456 -> no

print('Input number of yor ticket :')
ticket = int(input())
if ticket > 999999 or ticket < 100000:
    print('You input incorrect ticket number')
firstDigit = ticket // 100000
secondDigit = ticket // 10000 % 10
thirdDigit = ticket // 1000 % 10
fourthDigit = ticket // 100 % 10
fifthDigit = ticket // 10 % 10
sixthDigit = ticket % 10
summFirstDigits = firstDigit + secondDigit + thirdDigit
summSecondDigits = fourthDigit + fifthDigit + sixthDigit
if summFirstDigits == summSecondDigits :
    print('You took lucky ticket!Good job!=)')
else :
    print('It is not lucky ticket =( Try one more time' )
