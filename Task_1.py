# 1. Представлен список чисел. Необходимо вывести элементы исходного списка, значения которых больше предыдущего элемента. Use comprehension.
# in
# 9
# out
# [15, 16, 2, 3, 1, 7, 5, 4, 10]
# [16, 3, 7, 10]
# in
# 10
# out
# [28, 20, 10, 5, 1, 24, 7, 15, 23, 25]
# [24, 15, 23, 25]

a = [5, 2, 20, 34, 65]
c= []
for i in range(len(a) - 1):
    n = a[i]
    i += 1
    m = a[i]
    if m > n:
        c.append(m)
print(c) 
