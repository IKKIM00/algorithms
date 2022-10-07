n = int(input())
words = []
for i in range(n):
    words.append(str(input()))
answer = 0
for word in words:
    char_list = [word[0]]
    status = False
    for i in range(1, len(word)):
        if word[i] != word[i-1]:
            if word[i] in char_list:
                status = True
                continue
            else:
                char_list.append(word[i])
    if not status:
        answer += 1
print(answer)