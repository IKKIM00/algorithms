from collections import deque
from sys import stdin

input = stdin.readline

n = int(input())
initial_board = [list(map(int, input().split())) for _ in range(n)]
print(initial_board)