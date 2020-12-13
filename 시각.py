n = int(input())
t = 60
cnt = 0
for h in range(n + 1):
    for m in range(t):
        for s in range(t):
            if '3' in (str(h) + str(m) + str(s)):
                cnt += 1
print(cnt)