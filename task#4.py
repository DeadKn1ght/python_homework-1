# Задача 4: Петя, Катя и Сережа делают из бумаги журавликов. Вместе они сделали S журавликов.
# Сколько журавликов сделал каждый ребенок, если известно, что Петя и Сережа сделали одинаковое
# количество журавликов, а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?
# 6 -> 1  4  1
# 24 -> 4  16  4
# 60 -> 10  40  10

print('Input number of cranes equal 6 :')
S = int(input())
if S % 6 == 0:
    petrCranes = S // 6
    print(f'Petr made {petrCranes} cranes ')
    serjCranes = S // 6
    print(f'Serj made {serjCranes} cranes ')
    kateCranes = S // 6 * 4
    print(f'Kate made {kateCranes} cranes ')
else:
    print('You input incorrect number of cranes')
