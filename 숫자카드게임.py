# -*- coding: utf-8 -*-
"""
출처 - 2019 국가 교육기관 코딩 테스트
문제 설명 - 이것이 코딩 테스트다
입력값1
3 3
3 1 2
4 1 4
2 2 2

입력값2
2 4
7 3 1 8
3 3 3 4
"""

n, m = map(int, input().split())
result = 0
for i in range(n):
    data = list(map(int, input().split()))
    min_value = min(data)
    result = max(result, min_value)

print(result)
