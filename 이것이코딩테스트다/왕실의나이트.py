# -*- coding: utf-8 -*-

x_axis = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
y_axis = list(range(1, 9))

x = input()
y = int(input())

possible_routes = [(-2, 1), (-2, -1), (-1, 2), (-1, -2),
                   (2, 1), (2, -1), (1, 2), (1, -2)]
x_index = x_axis.index(x) + 1

answer = 0
for route in possible_routes:
    temp = (x_index + route[0], y + route[1])
    if temp[0] < 1 or temp[0] > 8 or temp[1] < 1 or temp[1] > 8:
        continue
    else:
        answer += 1
print(answer)