# 1.напечатать сторку в одну линию - C:\WINDOWS\System32\drivers\etc\nst
# print(\\C:\\WINDOWS\\System32\\drivers\\etc\\nst)
# print(r'C:\WINDOWS\System32\drivers\etc\nst')


# записать в список все буквы строки f=‘privet’
# s='privet'
# print(list(s))
# 



# преобразовать список таким образом
# a = [4, 3, -10, 1, 7, 12]
# [4, -10, 12, 3, 1, 7]
# выход

# a = [4, 3, -10, 1, 7, 12]
# b = [4, -10, 12, 3, 1, 7]
# res = [x for x in a if not x%2 ] + [x for x in a if  x%2 ]
# print(res)

# a = [4, 3, -10, 1, 7, 12]
# a.sort(key=lambda x: x % 2 == 0, reverse=True)
# print(a)

# a = [4, 3, -10, 1, 7, 12]
# a.sort(key=lambda x: x%2)
# print(a)



# 3)На вход программы поступает список наименований рек, записанных в одну строчку через пробел. Необходимо отсортировать этот список в порядке убывания длин названий. Результат вывести в одну строчку через пробел.

# Sample Input:
# Лена Енисей Волга Дон
# Sample Output:
# Енисей Волга Лена Дон
# from nis import maps


# spisok =list(maps(str,input().split()))       
# s=(sorted(sorted(spisok), key = len))
# print(s[::1])

# s=sorted(input().split(), key=lambda x: len(x))[::-1]
# print(*s)


# 4)  Вводится строка. Требуется, используя введенную строку, сформировать N=10 пар кортежей в формате:

# (символ, порядковый индекс)

# Первый индекс имеет значение 0. Строка может быть короче 10 символов, а может быть и длиннее. То есть, число пар может быть 10 и менее. 
# 4. Напишите программу, которая подсчитает и выведет сумму квадратов всех двузначных чисел, делящихся на 9.
# При решении задачи используйте комбинацию функций filter, map, sum.

# Обратите внимание: на 9 должно делиться исходное двузначное число, а не его квадрат.


# s = input()

# lst = list(zip(s, range(10)))

# print(lst)

# 5. Напишите функцию triangle(a, b, c), которая принимает на вход три длины отрезков и определяет, можно ли из этих отрезков составить треугольник. 
# Входные данные
# Выходные данные
# triangle(1, 1, 2)
# Это не треугольник
# triangle(7, 6, 10)

# triangle = [1,1,2]
# triangle.sort()
# is_triangle = triangle[0] + triangle[1] > triangle[2]

# if is_triangle:
#     print('Это треугольник!')
# else:
#     print('Это не треугольник!')

# l = [i for i in range(10, 100)]
# l1 = list(filter(lambda x: x % 9 == 0, l))
# l2 = sum(list(map(lambda x: x**2, l1)))
# print(l2)


# kombination = [x**2 for x in range(10,100) if not x%9]
# print(sum(kombination))



# phone_book = read_csv('phonebook.csv')
# def read_csv(filename: str) -> list:
#     data = []
#     fields = ["Фамилия", "Имя", "Телефон", "Описание"]
#     with open(filename, 'r', encoding='utf-8') as fin:
#         for line in fin:
#             record = dict(zip(fields, line.strip().split(',')))
#             data.append(record)

#     return data

# def show_menu() -> int:
#     print("\nВыберите необходимое действие:\n"
#           "1. Отобразить весь справочник\n"
#           "2. Найти абонента по фамилии\n"
#           "3. Найти абонента по номеру телефона\n"
#           "4. Добавить абонента в справочник\n"
#           "5. Сохранить справочник в текстовом формате\n"
#           "6. Закончить работу")
#     choice = int(input())
#     return choice


