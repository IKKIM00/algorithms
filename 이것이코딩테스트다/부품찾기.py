"""
5
8 3 7 9 2
3
5 7 9
"""
n = int(input())    # 가게에 있는 부품의 개수
store_stock = list(map(int, input().split()))
store_stock.sort()

m = int(input())    # 손님이 요청한 부품의 개수
customer_ask = list(map(int, input().split()))

answer = []
for i in customer_ask:
    answer.append('yes') if i in store_stock else answer.append('no')
print(answer)