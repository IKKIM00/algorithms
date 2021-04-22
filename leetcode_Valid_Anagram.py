# -*- coding: utf-8 -*-

"""
문제 설명:
Given two strings s and t, return true if t is an anagram of s, and false otherwise.

예시:
Input: s = "anagram", t = "nagaram"
Output: true
"""

from collections import Counter


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_cnt = Counter(s)
        t_cnt = Counter(t)

        return s_cnt == t_cnt