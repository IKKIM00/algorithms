# -*- coding: utf-8 -*-

"""
문제 설명:
Given an integer n, return a string array answer (1-indexed) where:

answer[i] == "FizzBuzz" if i is divisible by 3 and 5.
answer[i] == "Fizz" if i is divisible by 3.
answer[i] == "Buzz" if i is divisible by 5.
answer[i] == i if non of the above conditions are true.

예시:
Input: n = 5
Output: ["1","2","Fizz","4","Buzz"]
"""
class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        answer = list()
        for i in range(1, n + 1):
            if i % 15 == 0:
                answer.append("FizzBuzz")
            elif i % 5 == 0:
                answer.append("Buzz")
            elif i % 3 == 0:
                answer.append("Fizz")
            else:
                answer.append(str(i))
        return answer