# Задача 8: Требуется определить, можно ли от шоколадки размером n × m долек отломить k долек,
# если разрешается сделать один разлом по прямой между дольками (то есть разломить шоколадку на два прямоугольника).
# 3 2 4 -> yes
# 3 2 1 -> no

print('Input size of your chocolate.')
print('First size is :')
n = int(input())
print('Second size is :')
m = int(input())
print('Input amount of pieces yor try to cut to create two rectangular chocolates :')
k = int(input())
if k < (n * m):
    if k % n == 0 or k % m == 0:
        print('Yes,you can cut a chocolate like this')
    else:
        print('Nope, you cant create two rectangular chocolates like this')
else:
        print('Nope, you cant create two rectangular chocolates like this')