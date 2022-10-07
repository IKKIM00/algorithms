n = int(input())
if n < 10:
    start_num, end_num = 0, n
else:
    start_num, end_num = int(str(n)[0]), int(str(n)[1])

answer = 1
new_num = int(str(end_num) + str(start_num+end_num)[-1])
while n != new_num:
    if new_num < 10:
        start_num, end_num = 0, new_num
    else:
        start_num, end_num = int(str(new_num)[0]), int(str(new_num)[1])
    new_num = int(str(end_num) + str(start_num + end_num)[-1])
    answer += 1
print(answer)
