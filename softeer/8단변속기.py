import sys
import copy
input = sys.stdin.readline

dct = list(map(int, input().split()))
org_dct = dct.copy()
if org_dct == sorted(dct):
    print("ascending")
elif org_dct == sorted(dct, reverse=True):
    print("descending")
else:
    print("mixed")