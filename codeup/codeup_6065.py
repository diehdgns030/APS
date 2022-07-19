# 문제
# 3개의 정수(a, b, c)가 입력되었을 때, 짝수만 출력해보자.

# 입력예시
# 1 2 4

# 출력예시
# 2
# 4

#풀이
a, b, c = map(int, input().split())
numbers = [a, b, c]
for num in numbers:
    if num %2 == 0:
        print(num)