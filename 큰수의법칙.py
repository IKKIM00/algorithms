# 2019 국가 교육 기관 코딩 테스트
"""
문제 설명:
다양한 수로 이루어진 배열이 있을 때, 주어진 수들을 M번 더하여 가장 큰 수를 만드는 법칙
단, 배열의 특정한 인덱스에 해당하는 수가 연속해서 K번을 초과해서 더해질 수는 없음

Args:
    N - 배열의 크기
    M - 숫자가 더해지는 횟수
    K - 큰수의 법칙에 따른 결과
"""

n, m, k = map(int, input().split())
data = list(map(int, input().split()))

data.sort(reverse=True)
cnt, res = m // k, m % k
num_list = data[:2]
answer = (num_list[0] * k * cnt) + (num_list[1] * res)
print(answer)
