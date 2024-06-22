# Задача №9. Решение в группах
# По данному целому неотрицательному n вычислите
# значение n!. N! = 1 * 2 * 3 * … * N (произведение всех
# чисел от 1 до N) 0! = 1 Решить задачу используя цикл
# while
# Input: 5
# Output: 120

# n = int(input())

# fact = 1
# count = 0
# while count < n:
#     count += 1
#     fact *=count
# print(fact)



# Задача №11. Решение в группах
# Дано натуральное число A > 1. Определите, каким по
# счету числом Фибоначчи оно является, то есть
# выведите такое число n, что φ(n)=A. Если А не
# является числом Фибоначчи, выведите число -1.
# Input: 5
# Output: 6

# n = int(input())

# n0 = 0
# n1 = 0
# n2 = 1
# i = 2

# while n0 < n:
#     n0 = n1 + n2
#     n1 = n2
#     n2 = n0
#     i += 1
#     if n0 > n:
#         i = -1

# print(i)


# Орел и решка

# Дана строка текста, состоящая из букв русского алфавита "О" и "Р". Буква "О" – соответствует выпадению Орла, а буква "Р" – соответствует выпадению Решки. Напишите программу, которая подсчитывает наибольшее количество подряд выпавших Решек.

# Формат входных данных
# На вход программе подается строка текста, состоящая из букв русского алфавита "О" и "Р".

# Формат выходных данных
# Программа должна вывести наибольшее количество подряд выпавших Решек.

# Примечание. Если выпавших Решек нет, то необходимо вывести число
# 0
# 0.

# Тестовые данные 🟢
# Sample Input 1:
# ОРРОРОРООРРРО
# Sample Output 1:
# 3
# Sample Input 2:
# ООООООРРРОРОРРРРРРР
# Sample Output 2:
# 7
# Sample Input 3:
# ООООРРРРОРОРРРРРРРРООРОРОРРРРРРРРРРРРРРРРРРРРРРРРРРРРРРР
# Sample Output 3:
# 31

# n = 'ООООРРРРОРОРРРРРРРРООРОРОРРРРРРРРРРРРРРРРРРРРРРРРРРРРРРР'
# o = 0
# om = 0
# p = 0
# pm = 0
# for i in n:
#     if i == 'О':
#         o += 1
#         om = o
#         p = 0
#     elif i == 'Р':
#         p += 1
#         pm = p
#         o = 0

# print(pm)


# o = 0
# r = 0
# for element in n:
#     if element == 0:
#         o += 1
#     elif element == 1:
#         r += 1

# print(max(o,r))




# c = [0, 1, 0, 1, 1, 1, 1, 0, 0]
# o = 0
# r = 0
# for element in c:
#     if element == 0:
#         o += 1
#     elif element == 1:
#         r += 1

# print(min(o,r))


# Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. Петя помогает Кате по математике.
# Он задумывает два натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать. Для этого Петя делает две подсказки. Он называет сумму этих чисел S и их произведение P. Помогите Кате отгадать задуманные Петей числа.
# Примечание: числа S и P задавать не нужно, они будут передаваться в тестах. В результате вы должны вывести все возможные пары чисел X и Y через пробел, такие что X <= Y.
# # s = int(input())

# # p = int(input())

# c = 0
# for x in range(s + p):
#     if c:
#         break
#     for y in range(s + p):
#         if x + y == s and x * y == p:
#             c = 1
#             print(*sorted([x, y]))
#             break



# # n=16
# for i in range(int(numberN)+1):
#     exp = << i
#      if exp <= numberN:
#             print(power)





# n=[1,2,3,4,5]

# i = int(input("Введите i:"))
# i= i%len(n)
# for i in range(i):
#     t=n.pop()
#     n.insert(0,t)
# print(n)


# Требуется вычислить, сколько раз встречается некоторое число k в массиве list_1.

# list_1 = [1, 2, 3, 4, 5]
# k = 3
# if "k" in list_1:
#     list_1.remove("k")
# print(list_1)


# list_1 = [1, 2, 3, 4, 5]
# k = 3
# count_k = list_1.count(k)
# print(count_k)

# def find_nearest_digit(number, digits):
#     return min(digits, key=lambda x: (abs(x - number), x))

# list_1 = [1, 2, 3, 4, 5]
# k = 6
# closest_digit = find_nearest_digit(k, list_1)
# print(closest_digit)

# 5

# def find_nearest_digit(number, digits):
#     """
#     Возвращает цифру, ближайшую к заданному числу number среди перечисленных в списке digits.

#     :param number: Число, к которому нужно найти ближайшую цифру.
#     :param digits: Список цифр для поиска ближайшей.
#     :return: Цифра, ближайшая к number среди digits.
#     """
#     return min(digits, key=lambda x: (x - number)  *  *  2)

# # Пример использования функции:
# number = 50
# digits = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# closest_digit = find_nearest_digit(number, digits)
# print(f"Цифра, ближайшая к {number}: {closest_digit}")


# ingl = {"A, E, I, O, U, L, N, S, T, R" : "1"}

# i = ingl.get('E')
# print(i)

# ingl = {"A, E, I, O, U, L, N, S, T, R" : "1", "D, G" : "2" , "B, C, M, P" : "3", "F, H, V, W, Y": "4", "K" : "5", "J, X" :"8", "Q, Z": "10" , "А, В, Е, И, Н, О, Р, С, Т" : "1", "Д, К, Л, М, П, У" : "2",
# "Б, Г, Ё, Ь, Я" : "3",
# "Й, Ы" : "4",
# "Ж, З, Х, Ц, Ч" : "5" ,
# "Ш, Э, Ю" : "8" ,
# "Ф, Щ, Ъ" : "10" }

# k = "ignore"
# word= k.upper()
# sum_of_numbers = 0

# for letter in word:
#     for keys, values in ingl.items():
#         if letter in keys:
#             sum_of_numbers += int(values)

# print(sum_of_numbers)


# Сергей Сердюк Задача No25. Решение в группах
# Напишите программу, которая принимает на вход строку, и отслеживает, сколько раз каждый символ уже встречался. Количество повторов добавляется к символам с помощью постфикса формата _n.
# Input: a a a b c a a d c d d
# Output: a a_1 a_2 b c a_3 a_4 d c_1 d_1 d_2
# Для решения данной задачи используйте функцию .split()
# 15 минут

# dict = {}
# string = "a a a b c a a d c d d"
# string_res = ""

# for i in string.split():
#     if i in dict:
#         string_res = string_res + i + "_" + str(dict[i]) + " "
#     else:
#         string_res = string_res + i + " "
#     dict[i] = 1 + dict.get(i, 0)
# print(string_res)


# факториал числа n через рекурсию

# f = int(input())


# def fac(n):
#     if n in [1]:
#         return 1
#     return fac(n-1) * n
# list_1 = []
# for i in range(1, 8):
#     list_1.append(fac(i))
# # print(list_1)

# def step(a, b):
#     if b == 1:
#         return a
#     return a  *  step(a, b - 1)

# a = 3
# b = 5
# print(step(a, b))


# #
# def multiply_recursive(a, b):
#     # Базовый случай рекурсии: если b равно 0, возвращаем 1 (любое число, умноженное на 0, равно 0)
#     if b == 0:
#         return 1
#     # Рекурсивный случай: уменьшаем b на 1 и умножаем a на результата предыдущего шага рекурсии
#     else:
#         return a  *  multiply_recursive(a, b - 1)

# # Пример использования функции:
# a = int(input("Введите число a: "))
# b = int(input("Введите число b: "))
# result = multiply_recursive(a, b)
# print(f"Результат: {result}")


# a = 3
# b = 5

# def sum(a, b):
#     if b == 0:
#         return a
#     return 1 + sum(a-1,b)
# a = 3
# b = 5
# print(sum(a, b))


# Задача No35. Решение в группах
# Напишите функцию, которая принимает одно число и проверяет, является ли оно простым
# Напоминание: Простое число - это число, которое имеет 2 делителя: 1 и n(само число)
# Input: 5 Output: yes
# 15 минут


# def Simple (Turn, dew=2):
#     if dew*dew>=Turn:
#         return True
#     elif Turn%dew==0:
#         return False
#     else:
#         return Simple(Turn, dew+1)
# print(Simple(23))


# Заполните массив элементами арифметической прогрессии.
# Её первый элемент a1 , разность d и количество элементов n будет задано автоматически.
# Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.



# a1 = 2
# d = 3
# n = 4

# На выходе:


# 2
# 5
# 8
# 11

# a1 = 2  # Первый элемент прогрессии
# d = 3  # Разность прогрессии
# n = 4  # Количество элементов прогрессии

# # Создаем пустой список для хранения элементов прогрессии
# progressive_list = []

# # Используем формулу для вычисления каждого элемента прогрессии
# for i in range(n):
#     # Вычисляем i-й элемент прогрессии
#     element = a1 + i  *  d
#     progressive_list.append(element)

# print(progressive_list)


# def print_operation_table(operation, num_rows=9, num_columns=9):
#     pritntedRows = 1
#     printedColumns = 1
#     if num_columns < 2 or num_rows < 2:
#         print('ОШИБКА! Размерности таблицы должны быть больше 2!')
#         return
#     maxLongNum = len(str(operation(num_columns, num_rows)))
#     while pritntedRows <= num_rows:
#         while printedColumns <= num_columns:
#             if maxLongNum < len(str(operation(printedColumns, pritntedRows))):
#                 maxLongNum = len(str(operation(printedColumns, pritntedRows)))
#                 printedColumns += 1
#             pritntedRows += 1
#             printedColumns = 1

#     pritntedRows = 0
#     printedColumns = 0
#     while pritntedRows <= num_rows:
#         row = []
#         while printedColumns <= num_columns:
#             if pritntedRows == 0:
#                 row.append(('{0: >' + f'{maxLongNum}' + '}').format(printedColumns))
#             elif printedColumns == 0:
#                 row.append(('{0: >' + f'{maxLongNum}' + '}').format(pritntedRows))
#             else:
#                 if maxLongNum > 1:
#                     numbOperation = operation(printedColumns, pritntedRows)
#                     row.append(('{0: >' + f'{maxLongNum}' + '}').format(numbOperation))
#                 else:
#                     row.append(str(operation(printedColumns, pritntedRows)))
#             printedColumns += 1

#         print(*row, sep=' ')
#         pritntedRows += 1
#         printedColumns = 0




# print_operation_table(lambda x, y: x / y, 4, 4)

# data = [1, 2, 3, 5, 8, 15, 23, 38]
# res = list(filter(lambda x: x % 2 == 0, data))
# squared_res = list(map(lambda x: x ** 2, res))
# print(res,squared_res)


