# Задача 2: Найдите сумму цифр трехзначного числа.
# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0)

print('Input your 3-rd digit number :')
number = int(input())
if number > 999 or number < 100 :
    print ('You input incorrect number')
else :
    firstDigit = number // 100
    secondDigit = number // 10 % 10
    thirdDigit = number % 10
    summDigits = firstDigit + secondDigit + thirdDigit
print('Summ of all digits in your number is :')
print(summDigits)