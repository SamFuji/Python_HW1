# 1 TASK Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.

# day = int(input('Введите день недели или день в году по порядку: '))
# if day %6 == 0 or day %7 == 0:
#     print('День ', +day, ' Является выходным')
# else:
#     print('День ', +day, ' является будним')


# 2 TASK Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

# x=[0, 1]
# y=[0, 1]
# z=[0, 1]
# for x in range(2):
#     for y in range(2):
#         for z in range(2):
#             print('x:', x, 'y:', y, 'z:', z)
#             print((not(x or y or z)) == (not (x) and not (y) and not(z)))
             


# 3 TASK Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, в которой находится эта точка (или на какой оси она находится).

# x = int(input('Введите координату X:  '))
# y = int(input('Введите координату y:  '))
# if y<0 and x>0:
#     print('Координаты находятся в первой четверти')
# elif y>0 and x>0:
#     print('Координаты находятся во второй четверти')
# elif y<0 and x<0:
#     print('Координаты находятся в третьей четверти')
# elif y>0 and x<0:
#     print('Координаты находятся в четвёртой четверти')
# else:
#     print('Координаты находятся на оси.')    
    


# 4 TASK Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат точек в этой четверти (x и y).

# square = int(input('Введите номер четверти:  '))
# while square < 1 or square > 4 :
#     square = int(input('Такой четверти не существует, введите число от 1 до 4: '))
# if square == 1 :
#     print('Координаты находятся в диапазоне y<0 and x>0 ')
# elif square == 2 :
#     print('Координаты находятся в диапазоне y>0 and x>0 ')
# elif square == 3 :
#     print('Координаты находятся в диапазоне y<0 and x<0 ')
# elif square == 4 :
#     print('Координаты находятся в диапазоне y>0 and x<0 ')
  

# 5 TASK Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.

# from math import sqrt

# x1 = int(input('Введите координаты точки x1:'))
# y1 = int(input('Введите координаты точки y1:'))
# x2 = int(input('Введите координаты точки x2:'))
# y2 = int(input('Введите координаты точки y2:'))

# cross = sqrt(((x1-x2)**2)+((y1-y2)**2))
# print(cross)


