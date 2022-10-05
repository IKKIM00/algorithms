# 11분 3
num = str(input())
idx = 0
list0, list1 = [], []
for i in range(1, len(num)):
    if num[i] != num[idx]:
        if num[i] == num[0]:
            list0.append(num[idx: i])
        else:
            list1.append(num[idx: i])
        idx = i
if num[idx] != num[0]:
    list0.append(num[idx:])
else:
    list1.append(num[idx:])

print(min(len(list0), len(list1)))

# 정답 코드
count0, count1 = 0, 0
if num[0] == '1':
    count0 += 1
else:
    count1 += 1

for i in range(len(num) - 1):
    if num[i] != num[i + 1]:
        if num[i + 1] == '1':
            count0 += 1
        else:
            count1 += 1
print(min(count1, count0))