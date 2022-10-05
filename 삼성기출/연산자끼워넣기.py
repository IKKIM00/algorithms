from sys import stdin
from itertools import permutations

input = stdin.readline
n = int(input())
nums = list(map(int, input().split()))
cnts = list(map(int, input().split()))
cals = ['+', '-', '*', '/']
cal_str = []
for i in range(4):
    cal_str.extend([cals[i]] * cnts[i])

coms = set(permutations(cal_str, sum(cnts)))


def calc(indicator, num0, num1):
    if indicator == '+':
        return num0 + num1
    elif indicator == '-':
        return num0 - num1
    elif indicator == '*':
        return num0 * num1
    elif indicator == '/':
        if num0 > 0:
            return num0 // num1
        else:
            return -(abs(num0) // num1 )


max_val, min_val = -(int(1e9)), int(1e9)
for com in coms:
    temp = nums[0]
    for i in range(1, len(nums)):
        temp = calc(com[i - 1], temp, nums[i])
    if temp >= max_val:
        max_val = temp
    if temp <= min_val:
        min_val = temp
print(max_val)
print(min_val)