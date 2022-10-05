"""
6 4
1 4
2 3
2 4
5 6
"""
# 특정 원소가 속한 집합 찾기
def find_parent(parent, x):
    if parent[x] != x:
        return find_parent(parent, parent[x])
    # return x -> 이렇게 호출할 경우 최상위에 있는 부모를 또 찾아야 한다는 문제가 있음
    return parent[x] # -> 이렇게 호출하게 되면 루트 노드에 빠르게 접근할 수 있음

# 두 원소가 속한 집합 합치기
def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


v, e = map(int, input().split())
parent = [0] * (v + 1) # 부모 테이블 초기화

# 부모 테이블 상에서, 부모를 자기 자신으로 초기화
for i in range(1, v + 1):
    parent[i] = i

# union 연산을 각각 수행
for i in range(e):
    a, b = map(int, input().split())
    union_parent(parent, a, b)

print('각 원소가 속한 집합: ', end=' ')
for i in range(1, v + 1):
    print(find_parent(parent, i), end=' ')
print()

print('부모 테이블: ', end='')
for i in range(1, v + 1):
    print(parent[i], end='')