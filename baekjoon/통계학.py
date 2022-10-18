import math
from collections import Counter
n = int(input())
num_list = []
for _ in range(n):
    num_list.append(int(input()))

avg = sum(num_list) / n
div = sum(num_list) // n
print(div, avg)
if avg > -0.5:
    print("?")
    if avg <= div + 0.5:
        print(div + 1)
    else:
        print(div)
else:
    if avg <= div - 0.5:
        print(div - 1)
    else:
        print(div)

sorted_num_list = sorted(num_list)
print(sorted_num_list[n // 2])

cnt = Counter(num_list)
cnt = {k: v for k, v in sorted(cnt.items(), key=lambda x: x[1], reverse=True)}
max_cnt = max(cnt.values())
cnt_list = []
for k, v in cnt.items():
    if v == max_cnt:
        cnt_list.append(k)
    elif v < max_cnt:
        break
cnt_list.sort()
if len(cnt_list) > 1:
    print(cnt_list[1])
else:
    print(cnt_list[0])

print(sorted_num_list[-1] - sorted_num_list[0])