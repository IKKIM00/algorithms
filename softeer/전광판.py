import sys
input = sys.stdin.readline

t = int(input())

button = {"0": [0, 1, 2, 4, 5, 6],
          "1": [2, 6],
          "2": [1, 2, 3, 4, 5],
          "3": [1, 2, 3, 5, 6],
          "4": [0, 2, 3, 6],
          "5": [0, 1, 3, 5, 6],
          "6": [0, 1, 3, 4, 5, 6],
          "7": [0, 1, 2, 6],
          "8": [0, 1, 2, 3, 4, 5, 6],
          "9": [0, 1, 2, 3, 5, 6],
          "-1": []}

for _ in range(t):
    a, b = map(str, input().split())
    a_display = ["-1"] * (5 - len(a)) + list(a)
    b_display = ["-1"] * (5 - len(b)) + list(b)
    # print(a_display, b_display)
    answer = 0
    for i in range(5):
        if a_display[i] != b_display[i]:
            a_but = button[a_display[i]]
            b_but = button[b_display[i]]
            # print(a_but, b_but)
            for a_ele in a_but:
                if a_ele not in b_but:  answer += 1
            for b_ele in b_but:
                if b_ele not in a_but:  answer += 1
    print(answer)
