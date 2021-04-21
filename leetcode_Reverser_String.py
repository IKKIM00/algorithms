# -*- coding: utf-8 -*-
"""
문제 설명:
주어진 string s를 reverse하는 것
그런데 새로운 변수에 할당하는 것이 아니라 주어진 변수만 활용해서 해야 함

예시:
Input: s = ["h","e","l","l","o"]
Output: ["o","l","l","e","h"]
"""

class Solution:
    def reverseString(self, s: List[str]) -> None:
        left, right = 0, len(s) - 1
        while left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1
