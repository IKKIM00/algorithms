# -*- coding: utf-8 -*-
"""
기출 - 2018 E 기업 알고리즘 대회
문제 설명 - 이것이 코딩테스트다

"""
n, k = map(int, input().split())
cnt = 0
while n != 1:
    if n % k == 0:
        n /= k
        cnt += 1
    else:
        n -= 1
        cnt += 1

print(cnt)