# 7분
num = str(input())

if len(num) == 1:
    print(int(num))
else:
    answer = int(num[0]) * int(num[1]) if int(num[0]) != 0 and int(num[1]) != 0 else int(num[0]) + int(num[1])
    for i in range(2, len(num)):
        if int(num[i]) != 0:
            answer *= int(num[i])
    print(answer)

# 정답 코드
result = int(num[0])
for i in range(1, len(num)):
    num = int(num[i])
    if num <= 1 or result <= 1:
        result += num
    else:
        result *= num
print(result)