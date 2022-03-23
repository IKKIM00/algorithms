"""
2
홍길동 95
이순신 77
"""
n = int(input())

student_info = []
for i in range(n):
    student_info.append((input().split()))
student_info = sorted(student_info, key=lambda x: x[1])

for student in student_info:
    print(student[0])
