# -*- coding: utf-8 -*-

"""
문제 설명:
Given an array nums of size n, return the majority element.

예시:
Input: nums = [2,2,1,1,1,2,2]
Output: 2
"""

from collections import Counter
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        cnt = dict(Counter(nums))
        cnt = sorted(cnt.items(), key=(lambda x: x[1]), reverse=True)
        return cnt[0][0]