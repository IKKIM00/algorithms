from collections import Counter

s = str(input())
s = s.upper()
cnt = Counter(s)
max_cnt = max(cnt.values())

answer = ''
for key, val in cnt.items():
    if val == max_cnt:
        answer += key
if len(answer) > 1:
    print('?')
else:
    print(answer)
