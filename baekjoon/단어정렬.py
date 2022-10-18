n = int(input())
word_list = []
for _ in range(n):
    word_list.append(str(input()))
word_list = list(set(word_list))
word_dict = {}
for word in word_list:
    if len(word) in word_dict:
        word_dict[len(word)].append(word)
    else:
        word_dict[len(word)] = [word]
word_dict = {key: sorted(val) for key, val in sorted(word_dict.items(), key=lambda x: x[0])}
for words in word_dict.values():
    for word in words:
        print(word)