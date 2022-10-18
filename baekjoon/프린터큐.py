from collections import deque
test_case = int(input())

def find_answer(que, answer):
    while que:
        imp, idx = que.popleft()
        if not que:
            answer += 1
            return answer
        if imp < max(que)[0]:
            que.append([imp, idx])
        elif imp >= max(que)[0]:
            answer += 1
            if idx == m and imp >= max(que)[0]:
                return answer

for _ in range(test_case):
    n, m = map(int, input().split())
    importance = list(map(int, input().split()))
    que = deque([])
    for i in range(n):
        que.append([importance[i], i])
    answer = find_answer(que, 0)
    print(answer)
