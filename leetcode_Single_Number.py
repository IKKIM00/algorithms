# -*- coding: utf-8 -*-
"""
문제 설명:
array nums가 주어졌을 때 한번만 등장한 경우를 찾기

예시:
Input: nums = [4,1,2,1,2]
Output: 4
"""
from collections import Counter

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        cnts = dict(Counter(nums))
        for nums, cnt in cnts.items():
            if cnt == 1:
                return nums