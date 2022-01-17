numbers = ["3", "34", "64"]

# for i in range(len(numbers)):
#     numbers[i] = int(numbers[i])
#
#
# numbers[2] = numbers[2] + 1
# print(numbers[2])
# -----------------------------

# map helps you to apply a function in all the elements of a lst or data structuring object
# with map, it could be done like this:
# numbers = list(map(int, numbers))
#
# n = numbers[2] = numbers[2] +  1
# print(n)

# --------------------
# def sq(a):
#     return a*a
#
# num = [2, 3, 4, 5, 6, 7, 345, 76, 8]
#
# square = list(map(sq, num))
# print(square)
# ---------------------------
# num = [2, 3, 4, 5, 6, 7, 345, 76, 8]
#
# square = list(map(lambda x: x * x, num))  #it won't take the sq function here!
# print(square)
# ---------------------------------------


# def square(a):
#     return a*a
#
# def cube(a):
#     return a*a*a
#
# func = [square, cube]
#
# for i in range(5):
#     val = list(map(lambda x:x(i), func))
#     print(val)
                        #lambda here is creating a funcion which is just
                        # providing the given value in the item 'i'
# -----------------------------------------------------------
# --------------filter--
# list_1 = [1,  2,  3,  4,  5,  6,  7,  8,  9]
# def is_greater_5 (num):
#     return num>5
#
# gr_5 = list(filter(is_greater_5, list_1))
# print(gr_5)
# ------------------------------------------------------------
# ------------reduce---
# lst = [1,2,3,4]
# num = 0
# for i in lst:
#     num = num + i
# print(num)
#
# from functools import reduce
# lst =[1,2,3,4]
# num = reduce(lambda x, y: x+y, lst)
# print(num)

