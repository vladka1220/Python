'''2 ввод данных
_________________________________________
2.1
text = "big data"
print(text[3:])
all_numbers = '0123456789'
print(all_numbers[:: 2])
_________________________________________
print('s', 't', 'u', sep='&', end='\n')
2.3
one = input()
two = input()
tree = input()
four = input()
print(two,tree,four, sep = one, end = '\n')

_________________________________________
name = input()
print('Привет,',name,end="!")

_________________________________________
a = int(input())
V = (a*a*a)
Sp = (6*(a*a))
print('Площадь полной поверхности = ' + (str(Sp)))
print('Объем = ' + (str(V)))
_________________________________________

a = int(input())
b = int(input())
print((3*((a+b)*(a+b)*(a+b)))+(275*(b*b))-127*a-41)
_________________________________________
Напишите программу, которая считывает целое число, после чего на экран выводится следующее и
предыдущее целое число с пояснительным текстом.
a = int(input())
print('Следующее за числом' +' '+ (str(a)) + ' ' + 'число: ' + str(a+1))
print('Для числа' + ' '+ (str(a)) + ' ' + 'предыдущее число: ' + str(a-1))

_________________________________________
 считает стоимость трех компьютеров, состоящих из монитора, системного блока, клавиатуры и мыши.
monitor = int(input())
system = int(input())
keyboard = int(input())
mouse = int(input())
print((monitor + system + keyboard + mouse) *3)

_________________________________________
# Чтение двух целых чисел
a = int(input())
b = int(input())

# Вычисление суммы, разности и произведения
sum_result = a + b
diff_result = a - b
prod_result = a * b

# Вывод результатов
print(f"{a} + {b} = {sum_result}")
print(f"{a} - {b} = {diff_result}")
print(f"{a} * {b} = {prod_result}")

или 

a = int(input())
b = int(input())
print(a, "+", b, "=", (a + b))
print(a, "-", b, "=", (a - b))
print(a, "*", b, "=", (a * b))
_________________________________________
Программа должна вывести 
n-ый член арифметической прогрессии.
a = int(input())
d = int(input())
n = int(input())
result = a + (n - 1) * d

print(result)

_________________________________________
Напишите программу, которая считывает целое положительное число 

x = int(input())
a = x*2
b = x*3
c = x*4
d = x*5
print(str(x) + '---' + str(a) + '---' + str(b) + '---' + str(c) + '---' + str(d))

2.5 Целочисленная арифметика.

a = 15 // (16 % 7)

16 % 7 равно 2 (потому что 16 делённое на 7 равно 2 с остатком 2).
15 // 2 равно 7 (потому что это целочисленное деление).
Итак, a равно 7.

b = 34 % a * 5 - 29 % 5 * 2

34 % 7 равно 6 (потому что 34 делённое на 7 равно 4 с остатком 6).
29 % 5 равно 4 (потому что 29 делённое на 5 равно 5 с остатком 4).
Теперь подставим значения:

b = 6 * 5 - 4 * 2
b = 30 - 8
b = 22.
print(a + b)

a + b = 7 + 22
a + b = 29.

a = 15 // (16 % 7)
b = 34 % a * 5 - 29 % 5 * 2
print(a + b) 
_________________________________________
Программа должна вывести n-ый член геометрической прогрессии.
# Чтение входных данных
a_1 = int(input())
q = int(input())
n = int(input())

# Вычисление n-го члена геометрической прогрессии
a_n = a_1 * (q**(n-1))

# Вывод результата
print(a_n)


'''
